# DEFI.md — Ariane

### Nom du défi
Création en continu d'une "trame hypertexte" de la séance publique

### Description courte
Pendant une séance publique, une équipe note à la main qui prend la parole, quel amendement est appelé et le résultat de chaque vote. Ariane écoute la séance et reconstitue ce fil automatiquement : chaque intervention est datée, son auteur identifié, et reliée à sa fiche officielle sur assemblee-nationale.fr.

### Porteur
Charlotte R.

### Description longue
Lors d'une séance publique à l'Assemblée nationale, une équipe (la « régie ») suit le débat en direct et note au fil de l'eau qui parle, quel amendement est examiné et comment se termine chaque vote. Elle relie ensuite ce fil aux fiches officielles des députés et des amendements. Ce travail est long, continu et difficile à tenir en temps réel.

**Ariane** le fait automatiquement, en écoutant la séance. C'est ce fil, daté et cliquable de bout en bout, que nous appelons la « trame hypertexte » : un compte rendu vivant où chaque nom, chaque amendement et chaque vote renvoie vers le document officiel correspondant.

Le projet se compose de quatre modules :

| Module | Rôle |
|--------|------|
| **Le tisseur** (B1) | Transcrit ce qui est dit, en déduit qui parle, et replace chaque intervention dans le programme de la séance. Chaque orateur, amendement et vote est relié à sa fiche officielle. |
| **La rediffusion** (B2) | Rejoue une séance déjà enregistrée comme si elle se déroulait maintenant. À chaque instant, le système ne voit que ce qui était connu à cet instant-là et ne connaît jamais la suite. |
| **L'enregistrement** (B3) | Pendant la séance, enregistre les quatre sources qui arrivent en direct — le programme de séance (le « dérouleur »), le suivi des amendements (l'application Eliasse de l'Assemblée), le sommaire vidéo saisi par la régie, et la vidéo elle-même — en notant l'heure exacte de chaque élément et sans doublons. |
| **L'interface** (B4) | L'écran : une frise chronologique cliquable, la vidéo synchronisée, et un panneau qui affiche côte à côte le résultat d'Ariane et la version officielle. |

**Notre règle d'or.** Ariane devine à l'oreille : elle ne recopie jamais ce que la régie a déjà tapé. Les listes publiques de l'Assemblée (députés, amendements) servent uniquement à retrouver l'identité exacte de ce qui a été *entendu*. Le sommaire saisi par la régie n'intervient qu'après coup, comme version de référence, pour vérifier si Ariane a vu juste — jamais pour fabriquer le fil.

La démo fonctionne sur un ordinateur portable ordinaire, sans connexion Internet et sans matériel spécialisé, grâce au mode démonstration qui rejoue une séance enregistrée à l'avance.

### Image principale
[[images/interface.jpg]]

### Contributeurs
- Axel Baudrillart
- Charlotte Raviart
- Timothée Moyret
- Alexis Loubière
- Imene Atek
- Geraud Benazet
- Adrien Sporrer

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
- [L'interface d'Ariane — frise chronologique de la séance et vidéo synchronisée](images/interface.jpg)
- [Démonstration filmée (2 min) — le fil se tisse pendant un scrutin public](images/demo-ariane.mp4)
- [Résultat d'un scrutin public, lu par Ariane sur l'écran officiel](images/screenshot-scrutin.png)

### Documents
- [Diapositives de présentation](docs/diapositives.pdf)
- [Comment fonctionne Ariane — principe et architecture](docs/architecture.pdf)
- [Les données utilisées par Ariane](docs/donnees.pdf)

### URL de démonstration
https://github.com/TMoyret/Hackathon_AN/raw/main/hackathon-an-2026/images/demo-ariane.mp4

### Installer et relancer la démonstration
Le code est public. L'enregistrement de séance que la démonstration rejoue ne l'est pas : vidéo, son et données représentent plusieurs gigaoctets, trop volumineux pour être publiés sur GitHub. **Cloner le dépôt ne suffit donc pas à relancer la démonstration** : il faut d'abord disposer d'un enregistrement, que le module « L'enregistrement » permet de constituer à partir d'une séance. Nous pouvons également en fournir un sur demande.

Une fois l'enregistrement en place, et son emplacement renseigné dans `docker-compose.yml` :

```bash
cd tricoteuses-ariane
./ariane.sh --launch
# ouvrir http://127.0.0.1:8080/demo.html
```

#### Diapositives de présentation
[Diapositives de présentation](docs/diapositives.pdf)
