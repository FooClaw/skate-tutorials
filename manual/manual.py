"""
Fiche Tutoriel : Le Manual
===========================
Le manual est un trick d'equilibre fondamental ou l'on roule
sur les deux roues arriere sans que le tail touche le sol.
"""

NOM = "Manual"
DIFFICULTE = "Debutant"
PREREQUIS = [
    "Savoir rouler en equilibre a vitesse moderee",
    "Etre a l'aise pour ajuster son poids sur la planche",
]

DESCRIPTION = (
    "Le manual consiste a rouler en equilibre sur les deux roues arriere, "
    "sans poser le tail au sol. C'est un trick de base qui developpe "
    "l'equilibre et le controle, essentiel pour les enchainements (combos)."
)

POSITION_PIEDS = {
    "pied_arriere": "Sur le tail ou juste au-dessus, pret a doser la bascule",
    "pied_avant": "Au niveau des vis avant, controle l'inclinaison de la planche",
}

ETAPES = [
    "1. Roule a vitesse moderee, genoux legerement flechis.",
    "2. Deplace ton poids vers l'arriere en appuyant doucement sur le tail.",
    "3. Leve les roues avant du sol en gardant le tail au-dessus du sol (ne pas racler).",
    "4. Equilibre-toi en ajustant la pression du pied avant et du pied arriere.",
    "5. Regarde devant toi, pas tes pieds. Utilise tes bras pour l'equilibre.",
    "6. Pour sortir, repose les roues avant doucement en ramenant le poids vers l'avant.",
]

ERREURS_COURANTES = [
    "Appuyer trop fort sur le tail -> le tail racle le sol et tu freines.",
    "Poids trop en arriere -> tu tombes en arriere.",
    "Poids trop en avant -> les roues avant retombent tout de suite.",
    "Regarder ses pieds -> perte d'equilibre, il faut fixer un point devant soi.",
    "Vitesse trop faible -> plus difficile de maintenir l'equilibre.",
]

CONSEILS = [
    "Le secret c'est les micro-ajustements : de tout petits mouvements de chevilles.",
    "Commence avec un objectif court : 1 metre, puis 2, puis 5.",
    "Une vitesse moderee aide a l'equilibre (pas trop lent, pas trop vite).",
    "Plie legerement les genoux, ca donne plus de marge de manoeuvre.",
    "Utilise tes bras comme un funambule pour compenser les desequilibres.",
    "Trace une ligne au sol et essaie de manual d'un bout a l'autre.",
]


def afficher_fiche():
    """Affiche la fiche tutoriel complete du Manual."""
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
