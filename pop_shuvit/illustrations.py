"""
Generation des illustrations SVG pour le tutoriel Pop Shuvit
==============================================================
Genere des schemas pour la position des pieds et les phases du pop shuvit.
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
COULEUR_ROTATION = "#8e44ad"

LARGEUR = 400
HAUTEUR = 300


def _dessiner_sol(d, y_sol):
    d.append(draw.Rectangle(0, y_sol, LARGEUR, HAUTEUR - y_sol, fill=COULEUR_SOL, opacity=0.15))
    d.append(draw.Line(0, y_sol, LARGEUR, y_sol, stroke=COULEUR_SOL, stroke_width=2))


def _dessiner_planche(d, x, y, angle=0, longueur=120):
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


def _dessiner_fleche(d, x1, y1, x2, y2, texte="", couleur=None):
    c = couleur or COULEUR_FLECHE
    d.append(draw.Line(x1, y1, x2, y2,
                       stroke=c, stroke_width=2,
                       marker_end=draw.Marker(-0.8, -0.5, 0.2, 0.5, scale=8,
                                              orient="auto",
                                              children=[draw.Lines(-0.8, -0.5, 0, 0, -0.8, 0.5,
                                                                   fill=c)])))
    if texte:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        d.append(draw.Text(texte, 12, mx + 5, my - 5,
                           fill=c, font_family="sans-serif", font_weight="bold"))


def generer_position_pieds():
    """Vue de dessus : position des pieds pour le pop shuvit."""
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

    # Pied arriere - dans la poche du tail
    d.append(draw.Ellipse(cx - 110, cy + 10, 22, 14,
                          fill=COULEUR_PIED_ARRIERE, opacity=0.7))
    _dessiner_label(d, "Pied arriere", cx - 110, cy - 35)
    _dessiner_label(d, "(poche du tail)", cx - 110, cy - 20)

    # Pied avant - milieu
    d.append(draw.Ellipse(cx + 20, cy, 22, 14,
                          fill=COULEUR_PIED_AVANT, opacity=0.7))
    _dessiner_label(d, "Pied avant", cx + 20, cy - 35)
    _dessiner_label(d, "(milieu, detendu)", cx + 20, cy - 20)

    _dessiner_label(d, "TAIL", cx - 130, cy + 45)
    _dessiner_label(d, "NOSE", cx + 130, cy + 45)

    d.save_svg(os.path.join(ASSETS_DIR, "position_pieds.svg"))
    return d


def generer_phase_scoop():
    """Phase 1 : Le scoop du tail."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    _dessiner_planche(d, 200, y_sol - 18, angle=-5)
    _dessiner_skater(d, 200, y_sol - 32, flexion=0.5)

    # Fleche scoop en arriere
    _dessiner_fleche(d, 155, y_sol - 15, 120, y_sol - 5, "SCOOP")

    # Fleche rotation
    d.append(draw.Arc(200, y_sol - 50, 30, 200, 340,
                      fill="none", stroke=COULEUR_ROTATION, stroke_width=2,
                      stroke_dasharray="4"))
    d.append(draw.Text("180", 11, 235, y_sol - 55,
                       fill=COULEUR_ROTATION, font_family="sans-serif", font_weight="bold"))

    _dessiner_label(d, "Phase 1 : Le Scoop", LARGEUR // 2, 25)
    _dessiner_label(d, "Pousse le tail en arriere avec la cheville", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase1_scoop.svg"))
    return d


def generer_phase_rotation():
    """Phase 2 : La planche tourne sous les pieds."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche en rotation (a 90 degres, vue de profil = fine)
    _dessiner_planche(d, 200, y_sol - 55, angle=45)
    _dessiner_skater(d, 200, y_sol - 70, hauteur_corps=70, flexion=0.5)

    # Fleche de rotation
    d.append(draw.Arc(200, y_sol - 55, 40, 180, 350,
                      fill="none", stroke=COULEUR_ROTATION, stroke_width=2.5,
                      marker_end=draw.Marker(-0.8, -0.5, 0.2, 0.5, scale=6,
                                             orient="auto",
                                             children=[draw.Lines(-0.8, -0.5, 0, 0, -0.8, 0.5,
                                                                  fill=COULEUR_ROTATION)])))

    # Corps droit
    d.append(draw.Text("Corps droit !", 11, 290, y_sol - 100,
                       fill=COULEUR_VERT, font_family="sans-serif", font_weight="bold"))
    _dessiner_fleche(d, 280, y_sol - 95, 220, y_sol - 85, couleur=COULEUR_VERT)

    _dessiner_label(d, "Phase 2 : Rotation", LARGEUR // 2, 25)
    _dessiner_label(d, "La planche tourne, le corps reste droit", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase2_rotation.svg"))
    return d


def generer_phase_catch():
    """Phase 3 : Rattraper la planche."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    # Planche a 180, en l'air
    _dessiner_planche(d, 200, y_sol - 50, angle=0)
    _dessiner_skater(d, 200, y_sol - 65, hauteur_corps=70, flexion=0.6)

    # Fleches pieds qui rattrapent
    _dessiner_fleche(d, 175, y_sol - 60, 170, y_sol - 50, couleur=COULEUR_PIED_ARRIERE)
    _dessiner_fleche(d, 225, y_sol - 60, 230, y_sol - 50, couleur=COULEUR_PIED_AVANT)

    d.append(draw.Text("CATCH!", 13, 310, y_sol - 55,
                       fill=COULEUR_VERT, font_family="sans-serif", font_weight="bold"))

    _dessiner_label(d, "Phase 3 : Catch", LARGEUR // 2, 25)
    _dessiner_label(d, "Rattrape la planche avec les pieds", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase3_catch.svg"))
    return d


def generer_phase_reception():
    """Phase 4 : Reception."""
    d = draw.Drawing(LARGEUR, HAUTEUR, origin=(0, 0))
    d.append(draw.Rectangle(0, 0, LARGEUR, HAUTEUR, fill=COULEUR_FOND))

    y_sol = 240
    _dessiner_sol(d, y_sol)

    _dessiner_planche(d, 200, y_sol - 18, angle=0)
    _dessiner_skater(d, 200, y_sol - 32, flexion=0.8)

    # Vis
    d.append(draw.Circle(160, y_sol - 18, 6,
                         fill="none", stroke=COULEUR_VERT, stroke_width=2))
    d.append(draw.Circle(240, y_sol - 18, 6,
                         fill="none", stroke=COULEUR_VERT, stroke_width=2))
    d.append(draw.Text("vis", 10, 155, y_sol - 2,
                       fill=COULEUR_TEXTE, font_family="sans-serif", text_anchor="middle"))
    d.append(draw.Text("vis", 10, 245, y_sol - 2,
                       fill=COULEUR_TEXTE, font_family="sans-serif", text_anchor="middle"))

    # Note rotation completee
    d.append(draw.Text("180 OK", 12, 310, y_sol - 40,
                       fill=COULEUR_VERT, font_family="sans-serif", font_weight="bold"))

    _dessiner_label(d, "Phase 4 : Reception", LARGEUR // 2, 25)
    _dessiner_label(d, "Atterris sur les vis, genoux flechis", LARGEUR // 2, 50)

    d.save_svg(os.path.join(ASSETS_DIR, "phase4_reception.svg"))
    return d


def generer_toutes_illustrations():
    """Genere toutes les illustrations SVG dans le dossier assets."""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    generer_position_pieds()
    generer_phase_scoop()
    generer_phase_rotation()
    generer_phase_catch()
    generer_phase_reception()
    print(f"5 illustrations generees dans {ASSETS_DIR}/")


if __name__ == "__main__":
    generer_toutes_illustrations()
