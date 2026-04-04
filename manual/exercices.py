"""
Exercices pratiques pour le Manual
====================================
Exercices cibles pour developper l'equilibre
et le controle necessaires au manual.
"""

EXERCICES = [
    {
        "nom": "Le balancier",
        "phase": 1,
        "cible": "Trouver le point d'equilibre",
        "description": (
            "A faible vitesse, bascule d'avant en arriere entre les roues avant "
            "et le tail. Leve les roues avant, repose-les, leve le tail, repose-le. "
            "Le but est de sentir les deux points de bascule."
        ),
        "duree": "3 minutes",
        "critere_reussite": "20 bascules d'affilee sans poser le pied",
        "erreur_a_corriger": "Mouvements trop brusques, il faut etre progressif",
    },
    {
        "nom": "Le fil invisible",
        "phase": 1,
        "cible": "Stabilite du manual a basse vitesse",
        "description": (
            "Trace une ligne droite a la craie (3 metres). Roule en manual "
            "en suivant cette ligne. La ligne t'aide a rester droit et donne "
            "un objectif de distance visuel."
        ),
        "duree": "5 minutes",
        "critere_reussite": "3 metres de manual en restant sur la ligne",
        "erreur_a_corriger": "Devier de la trajectoire ou racler le tail",
    },
    {
        "nom": "Le compteur",
        "phase": 2,
        "cible": "Duree du manual",
        "description": (
            "Compte dans ta tete pendant le manual : 1, 2, 3... "
            "Note ton record a chaque session. Essaie de battre ton "
            "score a chaque tentative."
        ),
        "duree": "10 minutes",
        "critere_reussite": "Tenir un manual pendant 5 secondes",
        "erreur_a_corriger": "Trop se crisper en comptant, rester detendu",
    },
    {
        "nom": "Les portes",
        "phase": 2,
        "cible": "Controle de la direction en manual",
        "description": (
            "Place des plots ou bouteilles tous les 2 metres en zigzag. "
            "Passe entre eux en manual sans reposer les roues avant. "
            "Ca developpe le controle directionnel."
        ),
        "duree": "10 minutes",
        "critere_reussite": "Passer 3 portes en un seul manual",
        "erreur_a_corriger": "Reposer les roues avant pour corriger la trajectoire",
    },
    {
        "nom": "Le manual pad",
        "phase": 3,
        "cible": "Manual sur un element sureleve",
        "description": (
            "Trouve un muret ou un banc bas (hauteur de trottoir). "
            "Monte dessus et fais un manual sur toute la longueur. "
            "L'element sureleve ajoute la pression de ne pas tomber des cotes."
        ),
        "duree": "15 minutes",
        "critere_reussite": "Manual complet sur un element de 3 metres minimum",
        "erreur_a_corriger": "Panique en hauteur, rester calme et confiant",
    },
    {
        "nom": "Le combo ollie-manual",
        "phase": 4,
        "cible": "Enchainement ollie vers manual",
        "description": (
            "Fais un ollie et atterris directement en manual sans reposer "
            "les roues avant. C'est la base de beaucoup de combos en skate. "
            "Commence par un petit ollie et un manual court."
        ),
        "duree": "15 minutes",
        "critere_reussite": "Ollie suivi de 3 metres de manual, 3 fois d'affilee",
        "erreur_a_corriger": "Atterrir a plat apres le ollie au lieu de basculer en manual",
    },
]


def afficher_exercices(phase=None):
    """Affiche les exercices, filtres par phase si specifie."""
    print("=== Exercices pratiques : Manual ===\n")

    exercices = EXERCICES
    if phase is not None:
        exercices = [e for e in EXERCICES if e["phase"] == phase]
        print(f"(Phase {phase} uniquement)\n")

    for ex in exercices:
        print(f"[Phase {ex['phase']}] {ex['nom']}")
        print(f"  Cible : {ex['cible']}")
        print(f"  {ex['description']}")
        print(f"  Duree : {ex['duree']}")
        print(f"  Reussite : {ex['critere_reussite']}")
        print(f"  Corrige : {ex['erreur_a_corriger']}")
        print()


if __name__ == "__main__":
    afficher_exercices()
