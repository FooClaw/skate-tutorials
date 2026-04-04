"""
Generation des illustrations SVG pour le tutoriel Manual
==========================================================
Genere des schemas pour la position des pieds et les phases du manual.
"""

import drawsvg as draw
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

COULEUR_PLANCHE = "#2d2d2d"
COULEUR_ROUES = "#555555"
COULEUR_SKATER = "#e07020"
COULEUR_SOL = "#8B7355"
COULEUR_FOND = "#faf8f5"
COULEUR_PIED_ARRIERE = "#c0392b"
COULEUR_PIED_AVANT = "#2980b9"
COULEUR_FLECHE = "#e07020"
COULEUR_TEXTE = "#333333"
COULEUR_VERT = "#27ae60"

LARGEUR = 400
HAUTEUR = 300


def _dessiner_sol(d, y_sol):
    d.append(draw.Rectangle(0, y_sol, LARGEUR, HAUTEUR - y_sol, fill=COULEUR_SOL, opacity=0.15))
    d.append(draw.Line(0, y_sol, LARGEUR, y_sol, stroke=COULEUR_SOL, stroke_width=2))


def _dessiner_planche(d, x, y, angle=0, longueur=120, epaisseur=8):
    g = draw.Group(transform=f"translate({x},{y}) rotate({angle})")
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
    for rx in [-longueur // 3, longueur // 3]:
        g.append(draw.Circle(rx, 10, 9, fill=COULEUR_ROUES))
        g.append(draw.Circle(rx, 10, 4, fill="#777"))
    d.append(g)


def _dessiner_skater(d, x, y_pieds, hauteur_corps=80, flexion=0):
    decalage_genoux = flexion * 20
    y_genoux = y_pieds - hauteur_corps * 0.4 + decalage_genoux
    y_hanches = y_pieds - hauteur_corps * 0.55
    y_epaules = y_pieds - hauteur_corps * 0.85
    y_tete = y_pieds - hauteur_corps

    d.append(draw.Line(x - 12, y_pieds, x - 5, y_genoux,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x - 5, y_genoux, x, y_hanches,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x + 12, y_pieds, x + 5, y_genoux,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x + 5, y_genoux, x, y_hanches,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x, y_hanches, x, y_epaules,
                       stroke=COULEUR_SKATER, stroke_width=4, stroke_linecap="round"))
    d.append(draw.Line(x, y_epaules, x - 20, y_epaules + 15,
                       stroke=COULEUR_SKATER, stroke_width=3, stroke_linecap="round"))
    d.append(draw.Line(x, y_epaules, x + 20, y_epaules + 15,
                       stroke=COULEUR_SKATER, stroke_width=3, stroke_linecap="round"))
    d.append(draw.Circle(x, y_tete, 10, fill=COULEUR_SKATER))


def _dessiner_label(d, texte, x, y):
    d.append(draw.Text(texte, 14, x, y,
                       fill=COULEUR_TEXTE, font_family="sans-serif",
                       text_anchor="middle", font_weight="bold"))


def _dessiner_fleche(d, x1, y1, x2, y2, texte=""):
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


def generer_position_pieds():
    """Vue de dessus : position des pieds pour le manual."""
    d = draw.Drawing(LARGEUR, 250, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, 250, fill=COULEUR_FOND))

    cx, cy = LARGEUR // 2, 125

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

    for vx in [cx - 80, cx + 80]:
        for vy in [cy - 15, cy + 15]:
            d.append(draw.Circle(vx, vy, 3, fill=COULEUR_PLANCHE))

    # Pied arriere - sur le tail
    d.append(draw.Ellipse(cx - 105, cy, 22, 14,
                          fill=COULEUR_PIED_ARRIERE, opacity=0.7))
    _dessiner_label(d, "Pied arriere", cx - 105, cy - 40)
    _dessiner_label(d, "(sur le tail)", cx - 105, cy - 25)

    # Pied avant - sur les vis avant
    d.append(draw.Ellipse(cx + 75, cy, 22, 14,
                          fill=COULEUR_PIED_AVANT, opacity=0.7))
    _dessiner_label(d, "Pied avant", cx + 75, cy - 40)
    _dessiner_label(d, "(vis avant)", cx + 75, cy - 25)

    _dessiner_label(d, "TAIL", cx - 130, cy + 45)
    _dessiner_label(d, "NOSE", cx + 130, cy + 45)

    d.save_svg(os.path.join(ASSETS_DIR, "position_pieds.svg"))
    return d


def generer_phase_bascule():
    """Phase 1 : Basculer le poids vers l'arriere."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche legerement inclinee (roues avant levees)
    _dessiner_planche(d, 200, y_sol - 18, angle=-8)
    _dessiner_skater(d, 205, y_sol - 35, flexion=0.4)

    # Fleche poids vers l'arriere
    _dessiner_fleche(d, 220, y_sol - 100, 180, y_sol - 100, "Poids")

    # Roues avant levees
    d.append(draw.Line(235, y_sol - 30, 235, y_sol - 5,
                       stroke=COULEUR_VERT, stroke_width=1, stroke_dasharray="4"))
    d.append(draw.Text("leve", 10, 245, y_sol - 15,
                       fill=COULEUR_VERT, font_family="sans-serif", font_weight="bold"))

    _dessiner_label(d, "Phase 1 : Bascule", LARGEUR // 2, 25)
    _dessiner_label(d, "Deplace le poids vers l'arriere", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase1_bascule.svg"))
    return d


def generer_phase_equilibre():
    """Phase 2 : Maintenir l'equilibre."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    _dessiner_planche(d, 200, y_sol - 18, angle=-8)
    _dessiner_skater(d, 205, y_sol - 35, flexion=0.3)

    # Fleches micro-ajustements
    d.append(draw.Line(170, y_sol - 55, 170, y_sol - 75,
                       stroke=COULEUR_FLECHE, stroke_width=1.5))
    d.append(draw.Line(170, y_sol - 55, 170, y_sol - 35,
                       stroke=COULEUR_FLECHE, stroke_width=1.5))
    d.append(draw.Text("micro-", 10, 140, y_sol - 60,
                       fill=COULEUR_FLECHE, font_family="sans-serif"))
    d.append(draw.Text("ajustements", 10, 130, y_sol - 48,
                       fill=COULEUR_FLECHE, font_family="sans-serif"))

    # Zone d'equilibre
    d.append(draw.Rectangle(155, y_sol - 80, 30, 50,
                            fill=COULEUR_VERT, opacity=0.15,
                            stroke=COULEUR_VERT, stroke_width=1, stroke_dasharray="4"))

    _dessiner_label(d, "Phase 2 : Equilibre", LARGEUR // 2, 25)
    _dessiner_label(d, "Micro-ajustements des chevilles", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase2_equilibre.svg"))
    return d


def generer_phase_distance():
    """Phase 3 : Augmenter la distance."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    _dessiner_planche(d, 200, y_sol - 18, angle=-8)
    _dessiner_skater(d, 205, y_sol - 35, flexion=0.3)

    # Fleche de direction / distance
    d.append(draw.Line(280, y_sol - 18, 370, y_sol - 18,
                       stroke=COULEUR_VERT, stroke_width=2, stroke_dasharray="6",
                       marker_end=draw.Marker(-0.8, -0.5, 0.2, 0.5, scale=8,
                                              orient="auto",
                                              children=[draw.Lines(-0.8, -0.5, 0, 0, -0.8, 0.5,
                                                                   fill=COULEUR_VERT)])))
    d.append(draw.Text("distance", 11, 320, y_sol - 28,
                       fill=COULEUR_VERT, font_family="sans-serif", font_weight="bold"))

    # Reperes de distance au sol
    for i, dist in enumerate(["1m", "3m", "5m"]):
        x = 290 + i * 40
        d.append(draw.Line(x, y_sol, x, y_sol + 10,
                           stroke=COULEUR_SOL, stroke_width=1))
        d.append(draw.Text(dist, 9, x, y_sol + 22,
                           fill=COULEUR_SOL, font_family="sans-serif", text_anchor="middle"))

    _dessiner_label(d, "Phase 3 : Distance", LARGEUR // 2, 25)
    _dessiner_label(d, "Augmente progressivement la distance", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase3_distance.svg"))
    return d


def generer_phase_sortie():
    """Phase 4 : Sortie propre du manual."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche a plat (sortie)
    _dessiner_planche(d, 200, y_sol - 18, angle=0)
    _dessiner_skater(d, 200, y_sol - 32, flexion=0.5)

    # Fleche poids vers l'avant
    _dessiner_fleche(d, 180, y_sol - 100, 220, y_sol - 100, "Poids")

    # 4 roues au sol
    d.append(draw.Circle(160, y_sol - 3, 5,
                         fill="none", stroke=COULEUR_VERT, stroke_width=2))
    d.append(draw.Circle(240, y_sol - 3, 5,
                         fill="none", stroke=COULEUR_VERT, stroke_width=2))
    d.append(draw.Text("4 roues au sol", 10, 200, y_sol + 18,
                       fill=COULEUR_VERT, font_family="sans-serif",
                       text_anchor="middle", font_weight="bold"))

    _dessiner_label(d, "Phase 4 : Sortie", LARGEUR // 2, 25)
    _dessiner_label(d, "Repose les roues avant en douceur", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase4_sortie.svg"))
    return d


def generer_toutes_illustrations():
    """Genere toutes les illustrations SVG dans le dossier assets."""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    generer_position_pieds()
    generer_phase_bascule()
    generer_phase_equilibre()
    generer_phase_distance()
    generer_phase_sortie()
    print(f"5 illustrations generees dans {ASSETS_DIR}/")


if __name__ == "__main__":
    generer_toutes_illustrations()
