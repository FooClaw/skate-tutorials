# CLAUDE.md - Skate Tutorials

## Projet

Fiches tutoriels pour apprendre les tricks de skateboard, structurees en modules Python.

## Stack

- Python 3.11+
- Gestion de projet avec `uv`
- Pas de dependances externes pour l'instant

## Structure

```
skate-tutorials/
  main.py            # Point d'entree
  ollie/             # Repertoire dedie au Ollie
    __init__.py
    ollie.py         # Fiche tutoriel (description, etapes, conseils)
    progression.py   # 4 phases d'apprentissage graduelles
    exercices.py     # Exercices pratiques cibles
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
```

## Travail en cours

- [x] Init projet avec uv
- [x] Structure tricks/ avec premiere fiche (Ollie)
- [ ] Ajouter d'autres tricks (kickflip, heelflip, shuvit...)
- [ ] Systeme de progression / ordre d'apprentissage
