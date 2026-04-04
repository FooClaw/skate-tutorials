"""
Fiche Tutoriel : Le Pop Shuvit
================================
Le pop shuvit est un trick ou la planche fait une rotation
de 180 degres sous tes pieds sans que ton corps tourne.
"""

NOM = "Pop Shuvit"
DIFFICULTE = "Debutant-Intermediaire"
PREREQUIS = [
    "Maitriser le ollie basique",
    "Etre a l'aise en roulant a vitesse moderee",
    "Savoir rattraper la planche avec les pieds apres un saut",
]

DESCRIPTION = (
    "Le pop shuvit (ou pop shuv-it) consiste a faire tourner la planche "
    "de 180 degres en backside (la planche tourne vers l'arriere) "
    "grace a une impulsion du pied arriere, tout en restant face a "
    "la direction de deplacement. C'est l'un des premiers tricks "
    "de rotation de planche a apprendre apres le ollie."
)

POSITION_PIEDS = {
    "pied_arriere": "Sur le tail, orteils dans le coin arriere cote talons (poche du tail)",
    "pied_avant": "Au milieu de la planche, detendu, pret a se lever pour laisser la planche tourner",
}

ETAPES = [
    "1. Roule a vitesse moderee, genoux flechis, poids centre.",
    "2. Place ton pied arriere dans la poche du tail (coin arriere cote talons).",
    "3. Pop le tail en poussant vers l'arriere avec la cheville (scoop). "
    "C'est un mouvement de grattage en arriere, pas juste un pop vers le bas.",
    "4. Leve le pied avant pour laisser la planche tourner librement sous toi.",
    "5. Reste au-dessus de la planche, le corps ne tourne pas. Garde les epaules droites.",
    "6. Repere la planche quand elle a fait 180, rattrape-la avec les pieds sur les vis.",
    "7. Atterris genoux flechis, poids centre, et roule.",
]

ERREURS_COURANTES = [
    "Tourner le corps avec la planche -> garde les epaules face a la direction.",
    "Pop sans scoop -> la planche ne tourne pas, c'est le mouvement en arriere qui cree la rotation.",
    "Pied avant qui bloque la rotation -> leve-le suffisamment pour que la planche passe.",
    "Ne pas regarder la planche -> suis-la du regard pour la rattraper au bon moment.",
    "Atterrir trop en avant ou en arriere -> reste bien centre au-dessus de la planche.",
]

CONSEILS = [
    "Le scoop vient de la cheville, pas de toute la jambe.",
    "Commence a l'arret ou tres lentement pour comprendre le scoop.",
    "Pense a gratter le tail vers l'arriere, pas juste a le frapper vers le bas.",
    "Le pied avant ne fait presque rien : il se leve, c'est tout.",
    "Essaie d'abord sans pop (shuvit simple) pour sentir la rotation.",
    "Filme-toi de cote pour verifier que ton corps reste droit.",
]


def afficher_fiche():
    """Affiche la fiche tutoriel complete du Pop Shuvit."""
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
