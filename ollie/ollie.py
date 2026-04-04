"""
Fiche Tutoriel : Le Ollie
=========================
Le ollie est LE trick fondamental du skateboard.
C'est la base de presque tous les autres tricks.
"""

NOM = "Ollie"
DIFFICULTE = "Debutant"
PREREQUIS = ["Savoir rouler en equilibre", "Etre a l'aise avec le pied arriere sur le tail"]

DESCRIPTION = (
    "Le ollie consiste a faire decoller la planche du sol sans utiliser les mains. "
    "C'est le premier trick aerien a maitriser."
)

POSITION_PIEDS = {
    "pied_arriere": "Sur le tail (l'extremite arriere), orteils centres",
    "pied_avant": "Au milieu de la planche, legerement en retrait des vis avant",
}

ETAPES = [
    "1. Roule a vitesse moderee, genoux flechis, regard vers l'avant.",
    "2. Frappe le tail au sol avec le pied arriere d'un coup sec.",
    "3. Au moment ou le tail touche le sol, saute en l'air avec les deux jambes.",
    "4. Glisse le cote de ton pied avant vers le nose pour egaliser la planche.",
    "5. Monte les genoux pour laisser la planche monter avec toi.",
    "6. Atterris avec les deux pieds au-dessus des vis, genoux flechis pour amortir.",
]

ERREURS_COURANTES = [
    "Ne pas frapper le tail assez fort -> la planche ne decolle pas.",
    "Sauter avant de frapper le tail -> le timing est decale.",
    "Ne pas glisser le pied avant -> la planche ne se met pas a plat en l'air.",
    "Atterrir sur un seul pied -> risque de chute, toujours viser les quatre vis.",
]

CONSEILS = [
    "Commence a l'arret sur l'herbe pour comprendre le mouvement.",
    "Filme-toi pour analyser ton geste.",
    "La cle c'est le timing entre le pop et le slide du pied avant.",
    "Entraine-toi 15-20 min par session, la regularite paye plus que la duree.",
]


def afficher_fiche():
    """Affiche la fiche tutoriel complete du Ollie."""
    print(f"=== {NOM} ===")
    print(f"Difficulte : {DIFFICULTE}\n")
    print(f"Description : {DESCRIPTION}\n")

    print("Prerequis :")
    for p in PREREQUIS:
        print(f"  - {p}")

    print("\nPosition des pieds :")
    for pied, position in POSITION_PIEDS.items():
        print(f"  {pied} : {position}")

    print("\nEtapes :")
    for etape in ETAPES:
        print(f"  {etape}")

    print("\nErreurs courantes :")
    for erreur in ERREURS_COURANTES:
        print(f"  - {erreur}")

    print("\nConseils :")
    for conseil in CONSEILS:
        print(f"  - {conseil}")


if __name__ == "__main__":
    afficher_fiche()
