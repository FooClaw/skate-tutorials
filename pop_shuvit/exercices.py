"""
Exercices pratiques pour le Pop Shuvit
=======================================
Exercices cibles pour maitriser le scoop,
la rotation et la reception du pop shuvit.
"""

EXERCICES = [
    {
        "nom": "Le scoop fantome",
        "phase": 1,
        "cible": "Mouvement du scoop",
        "description": (
            "Pose la planche sur l'herbe. Sans monter dessus, place ton pied "
            "sur le tail et entraine le mouvement de scoop : pousse le tail "
            "en arriere avec la cheville. La planche doit tourner sur place."
        ),
        "duree": "3 minutes",
        "critere_reussite": "La planche fait 180 a chaque scoop, 10 fois d'affilee",
        "erreur_a_corriger": "Pousser avec toute la jambe au lieu de la cheville",
    },
    {
        "nom": "Le shuvit tapis",
        "phase": 1,
        "cible": "Shuvit complet sans rouler",
        "description": (
            "Sur un tapis ou l'herbe (planche immobile), fais un shuvit complet : "
            "monte sur la planche, scoop, saute, rattrape. Le sol mou enleve "
            "la peur de tomber."
        ),
        "duree": "5 minutes",
        "critere_reussite": "10 shuvits rattrapes proprement sur le tapis",
        "erreur_a_corriger": "Le corps qui tourne avec la planche",
    },
    {
        "nom": "Le pop and catch",
        "phase": 2,
        "cible": "Combiner pop et scoop",
        "description": (
            "A l'arret, fais le pop shuvit mais concentre-toi uniquement "
            "sur rattraper la planche avec le pied avant. Le pied avant "
            "est ton guide pour savoir si la rotation est bonne."
        ),
        "duree": "10 minutes",
        "critere_reussite": "Le pied avant rattrape la planche au bon moment, 5 fois d'affilee",
        "erreur_a_corriger": "La planche qui tourne trop ou pas assez (doser le scoop)",
    },
    {
        "nom": "Le couloir",
        "phase": 2,
        "cible": "Pop shuvit en ligne droite",
        "description": (
            "Trace deux lignes paralleles a 50 cm d'ecart. Roule entre elles "
            "et fais un pop shuvit. Tu dois atterrir entre les lignes. "
            "Ca t'oblige a rester centre et droit."
        ),
        "duree": "10 minutes",
        "critere_reussite": "5 pop shuvits en atterrissant entre les lignes",
        "erreur_a_corriger": "Deriver sur le cote pendant le trick",
    },
    {
        "nom": "Le pop shuvit monte",
        "phase": 3,
        "cible": "Hauteur du pop shuvit",
        "description": (
            "Fais un pop shuvit en essayant de monter les genoux au maximum. "
            "Plus tu montes les genoux, plus la planche a de place pour "
            "tourner en dessous et plus le trick est propre."
        ),
        "duree": "10 minutes",
        "critere_reussite": "Pop shuvit avec planche a 10 cm du sol minimum",
        "erreur_a_corriger": "Ne pas monter les genoux, planche qui rase le sol",
    },
    {
        "nom": "Le combo manual-shuvit",
        "phase": 4,
        "cible": "Enchainement avec d'autres tricks",
        "description": (
            "Fais un manual de 2-3 metres puis sors avec un pop shuvit. "
            "C'est un combo classique qui a beaucoup de style. "
            "Le timing de la sortie est la cle."
        ),
        "duree": "15 minutes",
        "critere_reussite": "3 combos manual -> pop shuvit propres",
        "erreur_a_corriger": "Perdre l'equilibre en sortant du manual",
    },
]


def afficher_exercices(phase=None):
    """Affiche les exercices, filtres par phase si specifie."""
    print("=== Exercices pratiques : Pop Shuvit ===\n")

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
