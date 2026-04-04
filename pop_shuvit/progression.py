"""
Progression d'apprentissage du Pop Shuvit
==========================================
4 phases graduelles pour maitriser le pop shuvit.
"""

PHASES = [
    {
        "numero": 1,
        "nom": "Le Shuvit (sans pop)",
        "objectif": "Comprendre la rotation de la planche sans hauteur",
        "lieu": "Surface plane, a l'arret ou sur l'herbe",
        "duree_estimee": "2 a 4 sessions",
        "sous_etapes": [
            {
                "nom": "Scoop a l'arret",
                "description": "A l'arret, pousse le tail en arriere avec la cheville pour faire tourner la planche. Pas besoin de sauter haut.",
                "critere_reussite": "La planche fait 180 et tu la rattrapes avec les pieds.",
                "repetitions": "10 shuvits rattrapes d'affilee",
            },
            {
                "nom": "Shuvit en roulant",
                "description": "Roule tres lentement et fais un shuvit. Concentre-toi sur le scoop et la reception.",
                "critere_reussite": "5 shuvits propres en roulant sans perdre l'equilibre.",
                "repetitions": "5 reussites d'affilee",
            },
            {
                "nom": "Corps droit",
                "description": "Fais des shuvits en verifiant que tes epaules restent face a la direction.",
                "critere_reussite": "Le corps ne tourne pas du tout pendant le trick.",
                "repetitions": "5 shuvits avec corps parfaitement droit",
            },
        ],
    },
    {
        "numero": 2,
        "nom": "Ajouter le pop",
        "objectif": "Combiner le pop et le scoop pour un vrai pop shuvit",
        "lieu": "Surface plane et lisse",
        "duree_estimee": "3 a 7 sessions",
        "sous_etapes": [
            {
                "nom": "Pop shuvit a l'arret",
                "description": "A l'arret, combine le pop vers le bas et le scoop vers l'arriere en un seul mouvement.",
                "critere_reussite": "La planche decolle et tourne de 180.",
                "repetitions": "10 pop shuvits a l'arret",
            },
            {
                "nom": "Pop shuvit en roulant lentement",
                "description": "Roule a faible vitesse et fais un pop shuvit complet.",
                "critere_reussite": "Pop shuvit propre avec atterrissage sur les vis.",
                "repetitions": "5 reussites d'affilee",
            },
            {
                "nom": "Pop shuvit a vitesse normale",
                "description": "Augmente la vitesse progressivement.",
                "critere_reussite": "Pop shuvit stable a vitesse de croisiere.",
                "repetitions": "5 reussites d'affilee",
            },
        ],
    },
    {
        "numero": 3,
        "nom": "Hauteur et style",
        "objectif": "Pop shuvit plus haut et plus propre",
        "lieu": "Surface plane, skatepark",
        "duree_estimee": "5 a 10 sessions",
        "sous_etapes": [
            {
                "nom": "Pop shuvit avec hauteur",
                "description": "Force le pop pour faire monter la planche plus haut pendant la rotation.",
                "critere_reussite": "La planche monte a 10 cm ou plus du sol.",
                "repetitions": "5 pop shuvits hauts d'affilee",
            },
            {
                "nom": "Rattrape propre",
                "description": "Concentre-toi sur rattraper la planche en l'air avec les pieds, pas attendre qu'elle retombe.",
                "critere_reussite": "Tu catches la planche au point le plus haut.",
                "repetitions": "5 catches propres d'affilee",
            },
            {
                "nom": "Pop shuvit par-dessus un obstacle",
                "description": "Place un petit obstacle et fais un pop shuvit par-dessus.",
                "critere_reussite": "Passage propre avec pop shuvit complet.",
                "repetitions": "3 reussites d'affilee",
            },
        ],
    },
    {
        "numero": 4,
        "nom": "Variations et combos",
        "objectif": "Integrer le pop shuvit dans des enchainements",
        "lieu": "Skatepark, spot de rue",
        "duree_estimee": "Sessions regulieres, progression continue",
        "sous_etapes": [
            {
                "nom": "Frontside pop shuvit",
                "description": "Inverse la rotation : la planche tourne vers l'avant (frontside). Le scoop part vers l'avant.",
                "critere_reussite": "Frontside pop shuvit propre en roulant.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Manual -> Pop shuvit out",
                "description": "Fais un manual et sors avec un pop shuvit.",
                "critere_reussite": "Sortie propre en pop shuvit apres 2 metres de manual.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Pop shuvit en descente",
                "description": "Fais un pop shuvit en descendant une marche ou un ledge.",
                "critere_reussite": "Pop shuvit propre avec atterrissage stable.",
                "repetitions": "3 reussites d'affilee",
            },
        ],
    },
]


def afficher_progression():
    """Affiche la progression complete phase par phase."""
    print("=== Progression du Pop Shuvit ===\n")
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
