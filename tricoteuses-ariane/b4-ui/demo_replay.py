#!/usr/bin/env python3
"""Relecture causale HORS-LIGNE pour la démo B4 (aucun GPU, aucun réseau).

Rejoue les segments STT réels d'une séance (stt-offline-*.ndjson) dans les cœurs
PURS de B1 (weaver.Weaver + deduce.Deducer) avec les vrais référentiels
(acteurs/organes/derouleur), produit le fil `thread.ndjson`, puis :
  - sert  GET /thread     en SSE (backlog complet, comme B1 :8100),
  - sert  GET /video.mp4  en Range (la VOD, pour un rendu vidéo synchronisé).

Usage :
  python demo_replay.py --bundle <data/2026-06-26-evening> [--port 8100] [--serve]
  python demo_replay.py --bundle ... --generate-only   # écrit thread.ndjson et résume
"""
import argparse
import glob
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

B1 = os.path.join(os.path.dirname(__file__), "..")  # remplacé par --b1 si besoin


def load_json(path):
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            with open(path, encoding=enc) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    with open(path, encoding="utf-8", errors="replace") as f:
        return json.load(f)


def build_thread(bundle, b1_dir):
    sys.path.insert(0, b1_dir)
    import weaver as w
    import deduce

    actors = load_json(os.path.join(bundle, "referential", "acteurs.json"))
    organes = load_json(os.path.join(bundle, "referential", "organes.json"))

    agenda = deduce.AgendaIndex()
    snaps = sorted(glob.glob(os.path.join(bundle, "raw", "derouleur", "*.json")))
    folded = 0
    for p in snaps:
        try:
            agenda.update(load_json(p))
            folded += 1
        except Exception:
            pass

    seq = w.Seq()
    weaver = w.Weaver(seq=seq)
    deducer = deduce.Deducer(agenda, actors, organes, seq=seq)

    stt = glob.glob(os.path.join(bundle, "stt-offline-*.ndjson"))
    if not stt:
        raise SystemExit(f"pas de stt-offline-*.ndjson dans {bundle}")
    nodes = []
    with open(stt[0], encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            seg = json.loads(line)
            ev = {"type": "utterance", "beg": seg["beg"],
                  "end": seg.get("end"), "text": seg["text"]}
            for node in weaver.feed(ev):        # -> le nœud utterance
                nodes.append(node)
                for extra in deducer.feed(node):  # -> amendment/speaker/ballot déduits
                    nodes.append(extra)

    print(f"[build] {os.path.basename(stt[0])} : {len(nodes)} nœuds "
          f"({folded}/{len(snaps)} snapshots dérouleur, {len(actors)} acteurs)",
          file=sys.stderr)
    kinds = {}
    for n in nodes:
        if n["kind"] != "utterance":
            kinds[n["kind"]] = kinds.get(n["kind"], 0) + 1
    print(f"[build] déduits : {kinds}", file=sys.stderr)
    return nodes


def summarize(nodes):
    print("\n--- nœuds déduits (t en s) ---", file=sys.stderr)
    for n in nodes:
        if n["kind"] == "utterance":
            continue
        c = n.get("canonical", {})
        extra = ""
        if n["kind"] == "speaker":
            extra = f" call={n.get('call')} grp={n.get('groupe_label')}"
        if c.get("amendement_uid"):
            extra += f" uid=…{c['amendement_uid'][-8:]}"
        print(f"  {n['t']/1000:7.1f}  {n['kind']:9} {n['text']!r}{extra}", file=sys.stderr)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    nodes = []
    video_path = None

    def log_message(self, *a):
        pass

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")

    def do_GET(self):
        if self.path.startswith("/thread.json"):
            return self._thread_json()
        if self.path.startswith("/thread"):
            return self._thread()
        if self.path.startswith("/video"):
            return self._video()
        self.send_response(404); self.send_header("Content-Length", "0"); self.end_headers()

    def _thread_json(self):
        """Tout le fil en une réponse JSON qui SE TERMINE (réseau au repos -> capture)."""
        body = json.dumps(self.nodes, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def _thread(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self._cors()
        self.end_headers()
        try:
            for n in self.nodes:  # tout le backlog d'un coup (le front dédoublonne par seq)
                self.wfile.write(("data: " + json.dumps(n, ensure_ascii=False) + "\n\n").encode())
            self.wfile.flush()
            while True:           # garder la connexion ouverte (heartbeat SSE)
                time.sleep(15)
                self.wfile.write(b": keep-alive\n\n")
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _video(self):
        path = self.video_path
        if not path or not os.path.exists(path):
            self.send_response(404); self.send_header("Content-Length", "0"); self.end_headers()
            return
        size = os.path.getsize(path)
        rng = self.headers.get("Range")
        start, end = 0, size - 1
        if rng and rng.startswith("bytes="):
            s, _, e = rng[6:].partition("-")
            start = int(s) if s else 0
            end = int(e) if e else size - 1
            end = min(end, size - 1)
        length = end - start + 1
        self.send_response(206 if rng else 200)
        self.send_header("Content-Type", "video/mp4")
        self.send_header("Accept-Ranges", "bytes")
        if rng:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(length))
        self._cors()
        self.end_headers()
        try:
            with open(path, "rb") as f:
                f.seek(start)
                remaining = length
                while remaining > 0:
                    buf = f.read(min(1 << 20, remaining))
                    if not buf:
                        break
                    self.wfile.write(buf)
                    remaining -= len(buf)
        except (BrokenPipeError, ConnectionResetError):
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--b1", default=None, help="dir de b1-weaver (défaut: ../b1-weaver relatif au bundle repo)")
    ap.add_argument("--out", default=None, help="où écrire thread.ndjson")
    ap.add_argument("--port", type=int, default=8100)
    ap.add_argument("--generate-only", action="store_true")
    args = ap.parse_args()

    b1_dir = args.b1 or os.path.join(args.bundle, "..", "..", "b1-weaver")
    b1_dir = os.path.abspath(b1_dir)
    nodes = build_thread(os.path.abspath(args.bundle), b1_dir)
    summarize(nodes)

    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "thread.ndjson")
    with open(out, "w", encoding="utf-8") as f:
        for n in nodes:
            f.write(json.dumps(n, ensure_ascii=False) + "\n")
    print(f"[out] {out}", file=sys.stderr)

    if args.generate_only:
        return

    videos = glob.glob(os.path.join(os.path.abspath(args.bundle), "video", "*.mp4"))
    Handler.nodes = nodes
    Handler.video_path = videos[0] if videos else None
    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"[serve] SSE http://127.0.0.1:{args.port}/thread  "
          f"video={'/video.mp4' if Handler.video_path else '—'}", file=sys.stderr)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
