# DEFI.md — Ariane

### Nom du défi
**Ariane** — Tisser le fil vivant d'une séance de l'Assemblée nationale

### Description courte
Ariane fusionne le flux de parole (STT) avec les référentiels publics de l'Assemblée (dérouleur, amendements, acteurs) en un fil d'événements horodaté et hyperlié — déduisant *qui a dit quoi* et le résolvant en identifiants canoniques, comme le fait la régie à la main aujourd'hui.

### Porteur
Équipe **Tricoteuses** — porté par Timothée Moyret

### Description longue
Lors d'une séance publique à l'Assemblée nationale, la régie tisse à la main un fil d'événements (prise de parole, dépôt d'amendement, scrutin, vote) à partir du flux vidéo et des données publiques. Ce travail est chronophage et sujet aux erreurs.

**Ariane** automatise cette chaîne en 4 briques :

| Brique | Rôle |
|--------|------|
| **B1 — Weaver** | Transforme la transcription STT en un fil d'événements, projeté sur la trame du dérouleur et résolu en IDs canoniques (orateur, amendement, scrutin). |
| **B2 — Replay** | Rejoue causalement une séance capturée (sources + audio/vidéo) sous une horloge maîtresse, sans jamais fuiter de données postérieures à `t`. |
| **B3 — Capture** | Enregistre les 4 flux live (dérouleur, Eliasse, NVS, vidéo) avec horodatage et déduplication, puis gèle les référentiels en un instantané. |
| **B4 — UI** | Interface statique : frise chronologique cliquable + vidéo synchronisée + volet de vérification par la NVS (vérité terrain). |

**Invariant de conception.** Le fil est *déduit de la parole*, jamais recopié depuis les flux saisis à la main par la régie. Les listes publiques servent uniquement de référentiels pour résoudre ce qui a été *entendu* en IDs canoniques. La NVS est la vérité terrain pour la validation, jamais une entrée du weaver.

Le tout fonctionne hors-ligne sur un laptop, sans GPU, grâce au mode *démo* qui rejoue un bundle pré-capturé.

### Image principale
![Capture d'écran de l'interface Ariane](images/cover.png)

### Contributeurs
- Timothée Moyret
- Alexis Loubière

### Ressources utilisées
- [x] `an-dossiers-legislatifs` — Dossiers législatifs de l'Assemblée nationale (législature courante) ✺ Assemblée nationale
- [x] `an-amendements-xvii` — Amendements déposés à l'Assemblée nationale (législature actuelle) ✺ Assemblée nationale
- [x] `an-comptes-rendus` — Comptes rendus de la séance publique à l'Assemblée nationale (législature actuelle) ✺ Assemblée nationale
- [x] `an-votes-xvii` — Votes des députés (législature actuelle) ✺ Assemblée nationale
- [x] `an-deputes-en-exercice` — Députés en exercice ✺ Assemblée nationale
- [ ] `openfisca-france-parameters` — Base de données de paramètres ✺ OpenFisca
- [ ] `an-deputes-historique` — Historique des députés ✺ Assemblée nationale
- [ ] `an-deputes-senateurs-ministres-par-legislature` — Députés, sénateurs et ministres d'une législature ✺ Assemblée nationale
- [ ] `an-agenda-reunions` — Agenda des réunions à l'Assemblée nationale (législature courante) ✺ Assemblée nationale
- [ ] `an-questions-gouvernement` — Questions de l'Assemblée nationale au Gouvernement ✺ Assemblée nationale
- [ ] `an-questions-gouvernement-ecrites` — Questions écrites de l'Assemblée nationale au Gouvernement ✺ Assemblée nationale
- [ ] `an-questions-gouvernement-orales` — Questions orales de l'Assemblée nationale au Gouvernement ✺ Assemblée nationale
- [ ] `premier-ministre-legi` — Codes, lois et règlements consolidés ✺ Premier ministre
- [ ] `premier-ministre-dole` — Dossiers législatifs Légifrance ✺ Premier ministre
- [ ] `premier-ministre-jorf` — Édition ''Lois et décrets'' du Journal officiel ✺ Premier ministre
- [ ] `senat-dispositifs-textes` — Dispositifs des textes déposés ou adoptés au Sénat ✺ Sénat
- [ ] `senat-dossiers-legislatifs` — Dossiers législatifs du Sénat ✺ Sénat
- [ ] `senat-amendements` — Amendements déposés au Sénat ✺ Sénat
- [ ] `senat-senateurs` — Sénateurs ✺ Sénat
- [ ] `senat-questions-gouvernement` — Questions orales et écrites du Sénat au Gouvernement ✺ Sénat
- [ ] `senat-comptes-rendus` — Comptes rendus de la séance publique au Sénat ✺ Sénat
- [ ] `an-et-co-database-regroupement-toutes-donnees` — Base de données unifiée Parlement / Législation / Service Public ✺ Assemblée nationale & communauté
- [ ] `an-et-co-serveur-mcp-regroupement-toutes-donnees` — Serveur MCP - Accès unifié Parlement / Législation / Service Public ✺ Assemblée nationale & communauté
- [ ] `an-et-co-api-regroupement-toutes-donnees` — API - Accès unifié Parlement / Législation / Service Public ✺ Assemblée nationale & communauté
- [ ] `legiwatch-api-parlement` — API Parlement ✺ LegiWatch
- [ ] `legiwatch-database-parlement` — Base de données Parlement ✺ LegiWatch
- [ ] `legiwatch-serveur-mcp-parlement` — Serveur MCP Parlement ✺ LegiWatch

### Galerie
- [Interface principale — frise + vidéo](images/screenshot-ui.png)
- [Démo scrutin public](images/screenshot-scrutin.png)

### Documents
- [Spécification architecture](docs/specs/2026-06-26-hackathon-mockup-architecture-design.md)
- [Documentation des données](docs/data/)
- [Diapositives de présentation](docs/diapositives.pdf)

### URL de démonstration
https://ariane-an-tail86bcaa.ts.net/demo.html

### Déploiement Docker (démo)
```bash
cd tricoteuses-ariane
./ariane.sh --launch
tailscale funnel 8080
# ouvrir https://<machine>.ts.net/demo.html
```

### Diapositives de présentation
[Slides de présentation](docs/diapositives.pdf)
