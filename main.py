import sys

from ollie.ollie import afficher_fiche
from ollie.progression import afficher_progression
from ollie.exercices import afficher_exercices

USAGE = """Usage: uv run python main.py [commande]

Commandes disponibles:
  fiche        Affiche la fiche complete du Ollie (par defaut)
  progression  Affiche les 4 phases d'apprentissage
  exercices    Affiche les exercices pratiques
"""


def main():
    commande = sys.argv[1] if len(sys.argv) > 1 else "fiche"

    if commande == "fiche":
        afficher_fiche()
    elif commande == "progression":
        afficher_progression()
    elif commande == "exercices":
        afficher_exercices()
    else:
        print(f"Commande inconnue : {commande}")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
