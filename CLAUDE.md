# CLAUDE.md - Skate Tutorials

## Projet

Fiches tutoriels pour apprendre les tricks de skateboard, structurees en modules Python.

## Stack

- Python 3.11+
- Gestion de projet avec `uv`
- `drawsvg` pour la generation des illustrations SVG
- GitHub Pages (dossier `docs/`) pour le site statique

## Structure

```
skate-tutorials/
  main.py            # Point d'entree
  ollie/             # Repertoire dedie au Ollie
    __init__.py
    ollie.py         # Fiche tutoriel (description, etapes, conseils)
    progression.py   # 4 phases d'apprentissage graduelles
    exercices.py     # Exercices pratiques cibles
    illustrations.py # Generation des SVGs
    assets/          # SVGs generes (position pieds, 4 phases)
  docs/              # GitHub Pages
    index.html       # Page tutoriel Ollie avec illustrations
  .github/workflows/
    deploy-pages.yml # CI : genere les SVGs et deploie sur GitHub Pages
  pyproject.toml
  uv.lock
```

## Conventions

- Un repertoire par trick a la racine du projet
- Chaque repertoire de trick contient : ollie.py (fiche), progression.py (phases), exercices.py (pratique)
- Chaque module expose une fonction `afficher_*()` pour afficher son contenu
- Pas d'accents dans les chaines Python (compatibilite terminal)
- Langue : francais

## Commandes utiles

```bash
uv run python main.py              # Afficher la fiche Ollie (par defaut)
uv run python main.py progression  # Afficher les 4 phases d'apprentissage
uv run python main.py exercices    # Afficher les exercices pratiques
uv run python -m ollie.illustrations  # Regenerer les SVGs dans ollie/assets/
```

## Travail en cours

- [x] Init projet avec uv
- [x] Structure ollie/ avec fiche, progression, exercices
- [x] Illustrations SVG (position pieds + 4 phases du ollie)
- [x] GitHub Pages (docs/index.html)
- [x] GitHub Actions : deploy-pages.yml (genere SVGs + deploie sur push)
- [ ] Ajouter d'autres tricks (kickflip, heelflip, shuvit...)
- [ ] Systeme de progression / ordre d'apprentissage
