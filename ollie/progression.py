"""
Progression d'apprentissage du Ollie
=====================================
4 phases graduelles pour maitriser le ollie,
de l'arret complet jusqu'a l'utilisation en situation reelle.
"""

PHASES = [
    {
        "numero": 1,
        "nom": "Statique",
        "objectif": "Comprendre et memoriser les gestes de base a l'arret",
        "lieu": "Sur l'herbe ou un tapis (planche immobile)",
        "duree_estimee": "2 a 5 sessions",
        "sous_etapes": [
            {
                "nom": "Pop seul",
                "description": "Frappe le tail au sol avec le pied arriere sans sauter.",
                "critere_reussite": "Le nose se leve a chaque frappe, geste fluide et regulier.",
                "repetitions": "20 pops d'affilee sans perdre l'equilibre",
            },
            {
                "nom": "Slide seul",
                "description": "Pied avant pose a plat, glisse-le vers le nose en flechissant la cheville.",
                "critere_reussite": "Le mouvement est naturel, le pied remonte jusqu'aux vis avant.",
                "repetitions": "20 slides d'affilee",
            },
            {
                "nom": "Pop + slide combines",
                "description": "Frappe le tail, puis immediatement glisse le pied avant vers le nose.",
                "critere_reussite": "La planche decolle du sol meme legerement (2-3 cm).",
                "repetitions": "10 ollies statiques avec decollage visible",
            },
        ],
    },
    {
        "numero": 2,
        "nom": "En roulant lentement",
        "objectif": "Reproduire le geste en mouvement a faible vitesse",
        "lieu": "Surface plane et lisse (parking, terrain de basket)",
        "duree_estimee": "3 a 7 sessions",
        "sous_etapes": [
            {
                "nom": "Ollie en ligne droite",
                "description": "Roule a vitesse de marche et fais un ollie basique.",
                "critere_reussite": "La planche decolle et tu atterris en roulant droit.",
                "repetitions": "10 ollies propres d'affilee sans tomber",
            },
            {
                "nom": "Ollie avec timing",
                "description": "Concentre-toi sur le timing : pop sec, slide rapide, reception souple.",
                "critere_reussite": "La planche se met a plat en l'air avant l'atterrissage.",
                "repetitions": "10 ollies avec planche bien a plat en l'air",
            },
            {
                "nom": "Ollie a vitesse normale",
                "description": "Augmente progressivement la vitesse de roulage.",
                "critere_reussite": "Ollie stable a vitesse de croisiere normale.",
                "repetitions": "10 ollies propres a vitesse normale",
            },
        ],
    },
    {
        "numero": 3,
        "nom": "Par-dessus un obstacle",
        "objectif": "Ajouter de la hauteur et un objectif concret a viser",
        "lieu": "Surface plane avec obstacles progressifs",
        "duree_estimee": "5 a 10 sessions",
        "sous_etapes": [
            {
                "nom": "Obstacle rasant (2-3 cm)",
                "description": "Place un crayon ou une ficelle au sol et passe par-dessus.",
                "critere_reussite": "Tu passes l'obstacle sans le toucher, 5 fois d'affilee.",
                "repetitions": "5 passages propres consecutifs",
            },
            {
                "nom": "Obstacle moyen (5-10 cm)",
                "description": "Utilise une chaussette roulee ou une petite boite.",
                "critere_reussite": "Passage propre avec atterrissage stable.",
                "repetitions": "5 passages propres consecutifs",
            },
            {
                "nom": "Obstacle haut (15-20 cm)",
                "description": "Un cone, une bouteille couchee, ou une planche posee a plat.",
                "critere_reussite": "Passage propre avec marge visible au-dessus de l'obstacle.",
                "repetitions": "3 passages propres consecutifs",
            },
        ],
    },
    {
        "numero": 4,
        "nom": "En situation",
        "objectif": "Utiliser le ollie dans des contextes reels de skate",
        "lieu": "Spot de rue, skatepark, trottoirs",
        "duree_estimee": "Sessions regulieres, progression continue",
        "sous_etapes": [
            {
                "nom": "Monter un trottoir",
                "description": "Approche un trottoir bas de face et ollie pour monter dessus.",
                "critere_reussite": "Tu montes le trottoir proprement sans racler le tail.",
                "repetitions": "5 montees propres d'affilee",
            },
            {
                "nom": "Descendre une marche",
                "description": "Ollie en arrivant au bord d'une marche pour atterrir en bas.",
                "critere_reussite": "Atterrissage stable, genoux bien flechis.",
                "repetitions": "5 descentes propres d'affilee",
            },
            {
                "nom": "Enchainer plusieurs ollies",
                "description": "Fais 3 ollies d'affilee en roulant, espaces de quelques metres.",
                "critere_reussite": "3 ollies enchaines sans poser le pied au sol.",
                "repetitions": "3 series de 3 ollies",
            },
        ],
    },
]


def afficher_progression():
    """Affiche la progression complete phase par phase."""
    print("=== Progression du Ollie ===\n")
    for phase in PHASES:
        print(f"--- Phase {phase['numero']} : {phase['nom']} ---")
        print(f"Objectif : {phase['objectif']}")
        print(f"Lieu : {phase['lieu']}")
        print(f"Duree estimee : {phase['duree_estimee']}\n")

        for i, etape in enumerate(phase["sous_etapes"], 1):
            print(f"  {i}. {etape['nom']}")
            print(f"     {etape['description']}")
            print(f"     Reussite : {etape['critere_reussite']}")
            print(f"     Objectif : {etape['repetitions']}")
            print()


if __name__ == "__main__":
    afficher_progression()
