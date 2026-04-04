"""
Progression d'apprentissage du Manual
=======================================
4 phases graduelles pour maitriser le manual,
de l'equilibre de base jusqu'aux enchainements.
"""

PHASES = [
    {
        "numero": 1,
        "nom": "Trouver le point d'equilibre",
        "objectif": "Sentir le point de bascule et le controler a basse vitesse",
        "lieu": "Surface plane et lisse (parking, gymnase)",
        "duree_estimee": "2 a 5 sessions",
        "sous_etapes": [
            {
                "nom": "Bascule statique",
                "description": "A l'arret ou presque, appuie sur le tail pour lever les roues avant, puis repose-les. Repete pour sentir le point de bascule.",
                "critere_reussite": "Tu leves les roues avant sans racler le tail, 10 fois d'affilee.",
                "repetitions": "10 bascules controlees",
            },
            {
                "nom": "Manual 1 metre",
                "description": "En roulant lentement, leve les roues avant et tiens l'equilibre sur 1 metre.",
                "critere_reussite": "1 metre de manual sans racler le tail ni reposer les roues.",
                "repetitions": "5 reussites d'affilee",
            },
            {
                "nom": "Sortie propre",
                "description": "Apprends a reposer les roues avant en douceur pour sortir du manual.",
                "critere_reussite": "Sortie controlee sans claquement des roues avant.",
                "repetitions": "10 sorties propres",
            },
        ],
    },
    {
        "numero": 2,
        "nom": "Augmenter la distance",
        "objectif": "Tenir le manual de plus en plus longtemps",
        "lieu": "Surface plane avec reperes (lignes, plots)",
        "duree_estimee": "3 a 7 sessions",
        "sous_etapes": [
            {
                "nom": "Manual 3 metres",
                "description": "Place deux reperes a 3 metres d'ecart. Manual de l'un a l'autre.",
                "critere_reussite": "3 metres de manual propre.",
                "repetitions": "5 reussites d'affilee",
            },
            {
                "nom": "Manual 5 metres",
                "description": "Augmente la distance a 5 metres. Concentre-toi sur les micro-ajustements.",
                "critere_reussite": "5 metres de manual regulier.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Manual a vitesse variable",
                "description": "Essaie le manual a differentes vitesses pour comprendre l'effet sur l'equilibre.",
                "critere_reussite": "3 metres de manual a vitesse lente et a vitesse normale.",
                "repetitions": "3 reussites a chaque vitesse",
            },
        ],
    },
    {
        "numero": 3,
        "nom": "Manual sur des elements",
        "objectif": "Maintenir le manual sur des surfaces variees",
        "lieu": "Skatepark, trottoirs, bancs bas",
        "duree_estimee": "5 a 10 sessions",
        "sous_etapes": [
            {
                "nom": "Manual sur un trottoir",
                "description": "Monte sur un trottoir (ollie ou en montant de face) et enchaine un manual.",
                "critere_reussite": "Manual tenu sur 2 metres apres la montee.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Manual sur un muret / ledge",
                "description": "Manual sur un element sureleve et etroit (muret, banc bas).",
                "critere_reussite": "Manual tenu sur toute la longueur de l'element.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Manual long (10 metres+)",
                "description": "Sur surface plane, vise les 10 metres et plus.",
                "critere_reussite": "10 metres de manual sans poser ni racler.",
                "repetitions": "1 reussite propre",
            },
        ],
    },
    {
        "numero": 4,
        "nom": "Combos et enchainements",
        "objectif": "Integrer le manual dans des enchainements de tricks",
        "lieu": "Skatepark, spot de rue",
        "duree_estimee": "Sessions regulieres, progression continue",
        "sous_etapes": [
            {
                "nom": "Ollie -> Manual",
                "description": "Fais un ollie et atterris directement en manual.",
                "critere_reussite": "Ollie suivi de 2 metres de manual.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Manual -> Shuvit out",
                "description": "Termine un manual par un pop shuvit pour sortir.",
                "critere_reussite": "Sortie propre en shuvit apres 2 metres de manual.",
                "repetitions": "3 reussites d'affilee",
            },
            {
                "nom": "Manual -> Kickflip out",
                "description": "Termine un manual par un kickflip (trick avance).",
                "critere_reussite": "Kickflip propre en sortie de manual.",
                "repetitions": "1 reussite propre",
            },
        ],
    },
]


def afficher_progression():
    """Affiche la progression complete phase par phase."""
    print("=== Progression du Manual ===\n")
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
