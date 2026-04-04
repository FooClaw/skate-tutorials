"""
Exercices pratiques pour le Ollie
==================================
Exercices cibles pour travailler les points techniques
qui posent le plus de difficultes aux debutants.
"""

EXERCICES = [
    {
        "nom": "Le pop metronome",
        "phase": 1,
        "cible": "Puissance et regularite du pop",
        "description": (
            "A l'arret, frappe le tail au sol en rythme regulier comme un metronome. "
            "Compte 1-2-3-pop, 1-2-3-pop. Le but est d'avoir un son sec et identique "
            "a chaque frappe."
        ),
        "duree": "3 minutes",
        "critere_reussite": "20 pops consecutifs avec le meme son et la meme hauteur de nose",
        "erreur_a_corriger": "Pop mou ou irregulier",
    },
    {
        "nom": "Le slide chaussette",
        "phase": 1,
        "cible": "Technique du slide du pied avant",
        "description": (
            "Enfile une chaussette par-dessus ta chaussure sur le pied avant. "
            "Entraine le mouvement de slide : le tissu doit glisser facilement "
            "sur le grip. Ca aide a sentir la trajectoire du pied."
        ),
        "duree": "5 minutes",
        "critere_reussite": "Le pied remonte naturellement jusqu'au nose a chaque slide",
        "erreur_a_corriger": "Pied avant qui reste colle ou qui ne glisse pas assez haut",
    },
    {
        "nom": "Le ollie ligne",
        "phase": 2,
        "cible": "Timing et coordination pop + slide",
        "description": (
            "Trace une ligne a la craie sur le sol. Roule vers la ligne et fais "
            "un ollie pour la franchir. La ligne donne un repere visuel pour "
            "declencher le pop au bon moment."
        ),
        "duree": "10 minutes",
        "critere_reussite": "10 franchissements propres de la ligne sans la toucher",
        "erreur_a_corriger": "Ollie declenche trop tot ou trop tard par rapport a la ligne",
    },
    {
        "nom": "Le ollie mur",
        "phase": 2,
        "cible": "Hauteur du ollie",
        "description": (
            "Place-toi a cote d'un mur. Fais un ollie et essaie de laisser une marque "
            "de grip sur le mur avec le cote de ta chaussure avant. Mesure la hauteur "
            "de la marque pour suivre ta progression."
        ),
        "duree": "10 minutes",
        "critere_reussite": "Marque reguliere a 15 cm ou plus du sol",
        "erreur_a_corriger": "Planche qui ne monte pas assez haut (slide insuffisant)",
    },
    {
        "nom": "L'echelle d'obstacles",
        "phase": 3,
        "cible": "Progression en hauteur",
        "description": (
            "Prepare 5 obstacles de hauteurs croissantes : stylo (1 cm), chaussette "
            "(3 cm), canette couchee (7 cm), boite (12 cm), cone (18 cm). "
            "Passe-les dans l'ordre. Si tu rates, recommence a l'obstacle precedent."
        ),
        "duree": "15 minutes",
        "critere_reussite": "Passer les 5 obstacles d'affilee sans en toucher aucun",
        "erreur_a_corriger": "Manque de hauteur ou mauvais timing d'approche",
    },
    {
        "nom": "Le parcours ollie",
        "phase": 4,
        "cible": "Enchainement et endurance",
        "description": (
            "Installe 3 petits obstacles espaces de 3 metres. Roule et ollie "
            "chaque obstacle sans t'arreter. Augmente progressivement la vitesse "
            "et reduis l'espacement."
        ),
        "duree": "15 minutes",
        "critere_reussite": "3 passages complets sans rater d'obstacle ni poser le pied",
        "erreur_a_corriger": "Perte de vitesse ou d'equilibre entre les obstacles",
    },
]


def afficher_exercices(phase=None):
    """Affiche les exercices, filtres par phase si specifie."""
    print("=== Exercices pratiques : Ollie ===\n")

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
