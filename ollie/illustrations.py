"""
Generation des illustrations SVG pour le tutoriel Ollie
========================================================
Genere des schemas en vue de profil pour chaque phase du ollie,
plus une vue de dessus pour la position des pieds.
"""

import drawsvg as draw
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Palette
COULEUR_PLANCHE = "#2d2d2d"
COULEUR_ROUES = "#555555"
COULEUR_SKATER = "#e07020"
COULEUR_SOL = "#8B7355"
COULEUR_FOND = "#faf8f5"
COULEUR_PIED_ARRIERE = "#c0392b"
COULEUR_PIED_AVANT = "#2980b9"
COULEUR_FLECHE = "#e07020"
COULEUR_TEXTE = "#333333"

LARGEUR = 400
HAUTEUR = 300


def _dessiner_sol(d, y_sol):
    """Dessine le sol avec une ligne et un remplissage subtil."""
    d.append(draw.Rectangle(0, y_sol, LARGEUR, HAUTEUR - y_sol, fill=COULEUR_SOL, opacity=0.15))
    d.append(draw.Line(0, y_sol, LARGEUR, y_sol, stroke=COULEUR_SOL, stroke_width=2))


def _dessiner_planche(d, x, y, angle=0, longueur=120, epaisseur=8):
    """Dessine la planche de skate en vue de profil."""
    g = draw.Group(transform=f"translate({x},{y}) rotate({angle})")
    # Planche avec courbure (nose et tail releves)
    g.append(draw.Path(
        fill=COULEUR_PLANCHE, stroke=COULEUR_PLANCHE, stroke_width=1,
        d=(
            f"M {-longueur//2} 0 "
            f"Q {-longueur//2 - 8} {-12}, {-longueur//2 + 5} {-14} "
            f"L {longueur//2 - 5} {-4} "
            f"Q {longueur//2 + 8} {-12}, {longueur//2} 0 "
            f"Z"
        ),
    ))
    # Roues
    for rx in [-longueur // 3, longueur // 3]:
        g.append(draw.Circle(rx, 10, 9, fill=COULEUR_ROUES))
        g.append(draw.Circle(rx, 10, 4, fill="#777"))
    d.append(g)


def _dessiner_skater(d, x, y_pieds, hauteur_corps=80, flexion=0):
    """Dessine un skater simplifie (bonhomme baton) en vue de profil."""
    # flexion : 0 = droit, 1 = genoux bien flechis
    decalage_genoux = flexion * 20
    y_genoux = y_pieds - hauteur_corps * 0.4 + decalage_genoux
    y_hanches = y_pieds - hauteur_corps * 0.55
    y_epaules = y_pieds - hauteur_corps * 0.85
    y_tete = y_pieds - hauteur_corps

    # Jambes
    d.append(draw.Line(x - 12, y_pieds, x - 5, y_genoux,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x - 5, y_genoux, x, y_hanches,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x + 12, y_pieds, x + 5, y_genoux,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x + 5, y_genoux, x, y_hanches,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    # Tronc
    d.append(draw.Line(x, y_hanches, x, y_epaules,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    # Bras
    d.append(draw.Line(x, y_epaules, x - 20, y_epaules + 15,
                       stroke=COULEUR_SKATER, stroke_width=3, stroke_linecap="round"))
    d.append(draw.Line(x, y_epaules, x + 20, y_epaules + 15,
                       stroke=COULEUR_SKATER, stroke_width=3, stroke_linecap="round"))
    # Tete
    d.append(draw.Circle(x, y_tete, 10, fill=COULEUR_SKATER))


def _dessiner_fleche(d, x1, y1, x2, y2, texte=""):
    """Dessine une fleche avec un texte optionnel."""
    d.append(draw.Line(x1, y1, x2, y2,
                       stroke=COULEUR_FLECHE, stroke_width=2,
                       marker_end=draw.Marker(-0.8, -0.5, 0.2, 0.5, scale=8,
                                              orient="auto",
                                              children=[draw.Lines(-0.8, -0.5, 0, 0, -0.8, 0.5,
                                                                   fill=COULEUR_FLECHE)])))
    if texte:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        d.append(draw.Text(texte, 12, mx + 5, my - 5,
                           fill=COULEUR_FLECHE, font_family="sans-serif", font_weight="bold"))


def _dessiner_label(d, texte, x, y):
    """Ajoute un label de texte."""
    d.append(draw.Text(texte, 14, x, y,
                       fill=COULEUR_TEXTE, font_family="sans-serif",
                       text_anchor="middle", font_weight="bold"))


def generer_position_pieds():
    """Vue de dessus : position des pieds sur la planche."""
    d = draw.Drawing(LARGEUR, 250, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, 250, fill=COULEUR_FOND))

    cx, cy = LARGEUR // 2, 125

    # Planche vue de dessus
    d.append(draw.Path(
        fill="#e8e0d4", stroke=COULEUR_PLANCHE, stroke_width=2,
        d=(
            f"M {cx - 130} {cy} "
            f"Q {cx - 140} {cy - 22}, {cx - 115} {cy - 25} "
            f"L {cx + 115} {cy - 25} "
            f"Q {cx + 140} {cy - 22}, {cx + 130} {cy} "
            f"Q {cx + 140} {cy + 22}, {cx + 115} {cy + 25} "
            f"L {cx - 115} {cy + 25} "
            f"Q {cx - 140} {cy + 22}, {cx - 130} {cy} "
            f"Z"
        ),
    ))

    # Vis (reperes)
    for vx in [cx - 80, cx + 80]:
        for vy in [cy - 15, cy + 15]:
            d.append(draw.Circle(vx, vy, 3, fill=COULEUR_PLANCHE))

    # Pied arriere (tail)
    d.append(draw.Ellipse(cx - 95, cy, 22, 14,
                          fill=COULEUR_PIED_ARRIERE, opacity=0.7))
    _dessiner_label(d, "Pied arriere", cx - 95, cy - 40)
    _dessiner_label(d, "(sur le tail)", cx - 95, cy - 25)

    # Pied avant (milieu)
    d.append(draw.Ellipse(cx + 20, cy, 22, 14,
                          fill=COULEUR_PIED_AVANT, opacity=0.7))
    _dessiner_label(d, "Pied avant", cx + 20, cy - 40)
    _dessiner_label(d, "(milieu / vis avant)", cx + 20, cy - 25)

    # Labels extremites
    _dessiner_label(d, "TAIL", cx - 130, cy + 45)
    _dessiner_label(d, "NOSE", cx + 130, cy + 45)

    d.save_svg(os.path.join(ASSETS_DIR, "position_pieds.svg"))
    return d


def generer_phase_pop():
    """Phase 1 : Le pop - frapper le tail au sol."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche inclinee (tail au sol)
    _dessiner_planche(d, 200, y_sol - 15, angle=-15)

    # Skater
    _dessiner_skater(d, 200, y_sol - 30, flexion=0.6)

    # Fleche du pop vers le bas
    _dessiner_fleche(d, 155, y_sol - 50, 155, y_sol - 10, "POP!")

    # Fleche nose qui monte
    _dessiner_fleche(d, 255, y_sol - 40, 255, y_sol - 80)

    _dessiner_label(d, "Phase 1 : Le Pop", LARGEUR // 2, 25)
    _dessiner_label(d, "Frappe le tail au sol d'un coup sec", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase1_pop.svg"))
    return d


def generer_phase_slide():
    """Phase 2 : Le slide - glisser le pied avant vers le nose."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche en l'air, inclinee
    _dessiner_planche(d, 200, y_sol - 60, angle=-10)

    # Skater en l'air
    _dessiner_skater(d, 200, y_sol - 75, flexion=0.3)

    # Fleche slide du pied avant
    _dessiner_fleche(d, 210, y_sol - 70, 260, y_sol - 85, "SLIDE")

    _dessiner_label(d, "Phase 2 : Le Slide", LARGEUR // 2, 25)
    _dessiner_label(d, "Glisse le pied avant vers le nose", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase2_slide.svg"))
    return d


def generer_phase_air():
    """Phase 3 : En l'air - planche a plat au point culminant."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche a plat en hauteur
    _dessiner_planche(d, 200, y_sol - 100, angle=0)

    # Skater en l'air, genoux montes
    _dessiner_skater(d, 200, y_sol - 115, hauteur_corps=65, flexion=0.8)

    # Fleche hauteur
    d.append(draw.Line(320, y_sol, 320, y_sol - 100,
                       stroke=COULEUR_FLECHE, stroke_width=1, stroke_dasharray="4"))
    d.append(draw.Text("hauteur", 11, 330, y_sol - 50,
                       fill=COULEUR_FLECHE, font_family="sans-serif"))

    _dessiner_label(d, "Phase 3 : En l'air", LARGEUR // 2, 25)
    _dessiner_label(d, "Planche a plat, genoux montes", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase3_air.svg"))
    return d


def generer_phase_reception():
    """Phase 4 : Reception - atterrir genoux flechis sur les vis."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche au sol
    _dessiner_planche(d, 200, y_sol - 18, angle=0)

    # Skater en flexion d'atterrissage
    _dessiner_skater(d, 200, y_sol - 32, flexion=0.9)

    # Fleches vers les vis
    d.append(draw.Circle(160, y_sol - 18, 6,
                         fill="none", stroke=COULEUR_PIED_ARRIERE, stroke_width=2))
    d.append(draw.Circle(240, y_sol - 18, 6,
                         fill="none", stroke=COULEUR_PIED_AVANT, stroke_width=2))
    d.append(draw.Text("vis", 10, 155, y_sol - 2,
                       fill=COULEUR_TEXTE, font_family="sans-serif", text_anchor="middle"))
    d.append(draw.Text("vis", 10, 245, y_sol - 2,
                       fill=COULEUR_TEXTE, font_family="sans-serif", text_anchor="middle"))

    _dessiner_label(d, "Phase 4 : Reception", LARGEUR // 2, 25)
    _dessiner_label(d, "Atterris sur les vis, genoux flechis", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase4_reception.svg"))
    return d


def generer_toutes_illustrations():
    """Genere toutes les illustrations SVG dans le dossier assets."""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    generer_position_pieds()
    generer_phase_pop()
    generer_phase_slide()
    generer_phase_air()
    generer_phase_reception()
    print(f"5 illustrations generees dans {ASSETS_DIR}/")


if __name__ == "__main__":
    generer_toutes_illustrations()
