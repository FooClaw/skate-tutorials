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
    ollie.py         # Fiche tutoriel du Ollie
  pyproject.toml
  uv.lock
```

## Conventions

- Un repertoire par trick a la racine du projet
- Chaque fiche contient : NOM, DIFFICULTE, PREREQUIS, DESCRIPTION, POSITION_PIEDS, ETAPES, ERREURS_COURANTES, CONSEILS
- Chaque module expose une fonction `afficher_fiche()` pour afficher le tutoriel
- Pas d'accents dans les chaines Python (compatibilite terminal)
- Langue : francais

## Commandes utiles

```bash
uv run python main.py           # Afficher la fiche du trick actuel
uv run python -m ollie.ollie    # Afficher la fiche Ollie directement
```

## Travail en cours

- [x] Init projet avec uv
- [x] Structure tricks/ avec premiere fiche (Ollie)
- [ ] Ajouter d'autres tricks (kickflip, heelflip, shuvit...)
- [ ] Systeme de progression / ordre d'apprentissage
