#!/usr/bin/env python3
"""
GEO-SEO PDF Report Generator
Génère des rapports PDF professionnels et prêts pour les clients à partir des données d'audit GEO.

Usage:
    python generate_pdf_report.py <fichier_json> [rapport.pdf]

Le fichier JSON doit contenir les résultats de l'audit structurés comme suit :
{
    "url": "https://exemple.com",
    "brand_name": "Exemple",
    "date": "2026-02-18",
    "geo_score": 62,
    "scores": { ... },
    "findings": { ... },
    ...
}

Ou passer les données JSON depuis stdin :
    cat audit_data.json | python generate_pdf_report.py - rapport.pdf
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.units import inch, mm
    from reportlab.lib.colors import (
        HexColor, black, white, grey, lightgrey, darkgrey,
        Color
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, HRFlowable, KeepTogether, Image as RLImage
    )
    from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics.charts.piecharts import Pie
    from reportlab.graphics import renderPDF
except ImportError:
    print("ERREUR : Packages requis non installés. Exécuter : pip install -r requirements.txt")
    sys.exit(1)


# ============================================================
# PALETTE DE COULEURS
# ============================================================
PRIMARY = HexColor("#1a1a2e")       # Bleu marine foncé
SECONDARY = HexColor("#16213e")     # Bleu marine légèrement plus clair
ACCENT = HexColor("#0f3460")        # Accent bleu
HIGHLIGHT = HexColor("#e94560")     # Rouge/corail
SUCCESS = HexColor("#00b894")       # Vert
WARNING = HexColor("#fdcb6e")       # Jaune/ambre
DANGER = HexColor("#d63031")        # Rouge
INFO = HexColor("#0984e3")          # Bleu
LIGHT_BG = HexColor("#f8f9fa")      # Fond clair
MEDIUM_BG = HexColor("#e9ecef")     # Fond moyen
TEXT_PRIMARY = HexColor("#2d3436")  # Texte foncé
TEXT_SECONDARY = HexColor("#636e72") # Texte gris
WHITE = white
BLACK = black


def get_score_color(score):
    """Retourne la couleur correspondant à la valeur du score."""
    if score >= 80:
        return SUCCESS
    elif score >= 60:
        return INFO
    elif score >= 40:
        return WARNING
    else:
        return DANGER


def get_score_label(score):
    """Retourne le niveau correspondant à la valeur du score."""
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Bon"
    elif score >= 55:
        return "Moyen"
    elif score >= 40:
        return "Insuffisant"
    else:
        return "Critique"


def create_score_gauge(score, width=120, height=120):
    """Crée une jauge visuelle de score."""
    d = Drawing(width, height)

    # Cercle de fond
    d.add(Circle(width/2, height/2, 50, fillColor=LIGHT_BG, strokeColor=lightgrey, strokeWidth=2))

    # Arc de score (simplifié en cercle coloré)
    color = get_score_color(score)
    d.add(Circle(width/2, height/2, 45, fillColor=color, strokeColor=None))

    # Cercle blanc intérieur
    d.add(Circle(width/2, height/2, 35, fillColor=WHITE, strokeColor=None))

    # Texte du score
    d.add(String(width/2, height/2 + 5, str(score),
                 fontSize=24, fontName='Helvetica-Bold',
                 fillColor=TEXT_PRIMARY, textAnchor='middle'))

    # Libellé
    d.add(String(width/2, height/2 - 12, "/100",
                 fontSize=10, fontName='Helvetica',
                 fillColor=TEXT_SECONDARY, textAnchor='middle'))

    return d


def create_bar_chart(data, labels, width=400, height=200):
    """Crée un graphique en barres horizontales pour les scores."""
    d = Drawing(width, height)

    chart = VerticalBarChart()
    chart.x = 60
    chart.y = 30
    chart.height = height - 60
    chart.width = width - 80
    chart.data = [data]
    chart.categoryAxis.categoryNames = labels
    chart.categoryAxis.labels.angle = 0
    chart.categoryAxis.labels.fontSize = 8
    chart.categoryAxis.labels.fontName = 'Helvetica'
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 100
    chart.valueAxis.valueStep = 20
    chart.valueAxis.labels.fontSize = 8

    # Colorier chaque barre selon le score
    for i, score in enumerate(data):
        chart.bars[0].fillColor = get_score_color(score)

    chart.bars[0].strokeColor = None
    chart.bars[0].strokeWidth = 0

    d.add(chart)
    return d


def create_platform_chart(platforms, width=450, height=180):
    """Crée un graphique des scores de maturité par plateforme."""
    d = Drawing(width, height)

    bar_height = 22
    bar_max_width = 280
    start_y = height - 30
    label_x = 10

    for i, (name, score) in enumerate(platforms.items()):
        y = start_y - (i * (bar_height + 10))

        # Nom de la plateforme
        d.add(String(label_x, y + 5, name,
                     fontSize=9, fontName='Helvetica',
                     fillColor=TEXT_PRIMARY, textAnchor='start'))

        # Barre de fond
        bar_x = 130
        d.add(Rect(bar_x, y, bar_max_width, bar_height,
                    fillColor=LIGHT_BG, strokeColor=None))

        # Barre de score
        bar_width = (score / 100) * bar_max_width
        color = get_score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                    fillColor=color, strokeColor=None))

        # Texte du score
        d.add(String(bar_x + bar_max_width + 10, y + 6, f"{score}/100",
                     fontSize=9, fontName='Helvetica-Bold',
                     fillColor=TEXT_PRIMARY, textAnchor='start'))

    return d


def build_styles():
    """Crée les styles de paragraphe personnalisés."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='ReportTitle',
        fontName='Helvetica-Bold',
        fontSize=28,
        textColor=PRIMARY,
        spaceAfter=6,
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        name='ReportSubtitle',
        fontName='Helvetica',
        fontSize=14,
        textColor=TEXT_SECONDARY,
        spaceAfter=20,
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=PRIMARY,
        spaceBefore=20,
        spaceAfter=10,
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        name='SubHeader',
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=ACCENT,
        spaceBefore=14,
        spaceAfter=6,
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        name='BodyText_Custom',
        fontName='Helvetica',
        fontSize=10,
        textColor=TEXT_PRIMARY,
        spaceBefore=4,
        spaceAfter=4,
        leading=14,
        alignment=TA_JUSTIFY,
    ))

    styles.add(ParagraphStyle(
        name='SmallText',
        fontName='Helvetica',
        fontSize=8,
        textColor=TEXT_SECONDARY,
        spaceBefore=2,
        spaceAfter=2,
    ))

    styles.add(ParagraphStyle(
        name='ScoreLabel',
        fontName='Helvetica-Bold',
        fontSize=36,
        textColor=PRIMARY,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name='HighlightBox',
        fontName='Helvetica',
        fontSize=10,
        textColor=TEXT_PRIMARY,
        backColor=LIGHT_BG,
        borderPadding=10,
        spaceBefore=8,
        spaceAfter=8,
        leading=14,
    ))

    styles.add(ParagraphStyle(
        name='CriticalFinding',
        fontName='Helvetica-Bold',
        fontSize=10,
        textColor=DANGER,
        spaceBefore=4,
        spaceAfter=2,
    ))

    styles.add(ParagraphStyle(
        name='Recommendation',
        fontName='Helvetica',
        fontSize=10,
        textColor=TEXT_PRIMARY,
        leftIndent=15,
        spaceBefore=3,
        spaceAfter=3,
        bulletIndent=5,
        leading=14,
    ))

    styles.add(ParagraphStyle(
        name='Footer',
        fontName='Helvetica',
        fontSize=8,
        textColor=TEXT_SECONDARY,
        alignment=TA_CENTER,
    ))

    return styles


def header_footer(canvas, doc):
    """Ajoute l'en-tête et le pied de page à chaque page."""
    canvas.saveState()

    # Filet d'en-tête
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(2)
    canvas.line(50, letter[1] - 40, letter[0] - 50, letter[1] - 40)

    # Texte d'en-tête
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(TEXT_SECONDARY)
    canvas.drawString(50, letter[1] - 35, "Rapport d'analyse GEO-SEO")

    # Pied de page
    canvas.setStrokeColor(lightgrey)
    canvas.setLineWidth(0.5)
    canvas.line(50, 40, letter[0] - 50, 40)

    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(TEXT_SECONDARY)
    canvas.drawString(50, 28, f"Généré le {datetime.now().strftime('%d %B %Y')}")
    canvas.drawRightString(letter[0] - 50, 28, f"Page {doc.page}")
    canvas.drawCentredString(letter[0] / 2, 28, "Confidentiel")

    canvas.restoreState()


def make_table_style(header_color=PRIMARY):
    """Crée un style de tableau cohérent."""
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), header_color),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TEXTCOLOR', (0, 1), (-1, -1), TEXT_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, lightgrey),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ])


def generate_report(data, output_path="GEO-RAPPORT.pdf"):
    """Génère le rapport PDF complet à partir des données d'audit."""

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=55,
        bottomMargin=55,
        leftMargin=50,
        rightMargin=50,
    )

    styles = build_styles()
    elements = []

    # Extraction des données avec valeurs par défaut
    url = data.get("url", "https://exemple.com")
    brand_name = data.get("brand_name", url.replace("https://", "").replace("http://", "").split("/")[0])
    date = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    geo_score = data.get("geo_score", 0)

    scores = data.get("scores", {})
    ai_citability = scores.get("ai_citability", 0)
    brand_authority = scores.get("brand_authority", 0)
    content_eeat = scores.get("content_eeat", 0)
    technical = scores.get("technical", 0)
    schema_score = scores.get("schema", 0)
    platform_optimization = scores.get("platform_optimization", 0)

    platforms = data.get("platforms", {
        "Google AI Overviews": 0,
        "ChatGPT": 0,
        "Perplexity": 0,
        "Gemini": 0,
        "Bing Copilot": 0,
    })

    crawlers = data.get("crawlers", [])
    findings = data.get("findings", [])
    quick_wins = data.get("quick_wins", [])
    medium_term = data.get("medium_term", [])
    strategic = data.get("strategic", [])
    executive_summary = data.get("executive_summary", "")
    crawler_access = data.get("crawler_access", {})
    schema_findings = data.get("schema_findings", {})
    content_findings = data.get("content_findings", {})
    technical_findings = data.get("technical_findings", {})
    brand_findings = data.get("brand_findings", {})

    # ============================================================
    # PAGE DE COUVERTURE
    # ============================================================
    elements.append(Spacer(1, 100))

    # Titre
    elements.append(Paragraph("Rapport d'analyse GEO", styles['ReportTitle']))
    elements.append(Spacer(1, 8))

    # Sous-titre
    elements.append(Paragraph(
        f"Audit d'optimisation pour les moteurs génératifs (GEO) — <b>{brand_name}</b>",
        styles['ReportSubtitle']
    ))

    elements.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=20))

    # Tableau des informations clés
    details_data = [
        ["Site web", url],
        ["Date d'analyse", datetime.strptime(date, "%Y-%m-%d").strftime("%d %B %Y") if "-" in date else date],
        ["Score GEO", f"{geo_score}/100 — {get_score_label(geo_score)}"],
    ]

    details_table = Table(details_data, colWidths=[120, 350])
    details_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), ACCENT),
        ('TEXTCOLOR', (1, 0), (1, -1), TEXT_PRIMARY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, lightgrey),
    ]))
    elements.append(details_table)

    elements.append(Spacer(1, 30))

    # Jauge de score
    gauge = create_score_gauge(geo_score, 200, 200)
    elements.append(gauge)

    elements.append(Spacer(1, 20))

    # Libellé du score
    score_color = get_score_color(geo_score)
    elements.append(Paragraph(
        f'<font color="{score_color.hexval()}">{get_score_label(geo_score)}</font>',
        ParagraphStyle('ScoreLabelColored', parent=styles['SectionHeader'],
                       alignment=TA_CENTER, fontSize=20)
    ))

    elements.append(PageBreak())

    # ============================================================
    # SYNTHÈSE EXÉCUTIVE
    # ============================================================
    elements.append(Paragraph("Synthèse exécutive", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    if executive_summary:
        elements.append(Paragraph(executive_summary, styles['BodyText_Custom']))
    else:
        elements.append(Paragraph(
            f"Ce rapport présente les résultats d'un audit complet d'optimisation pour les moteurs "
            f"génératifs (GEO) conduit sur <b>{brand_name}</b> ({url}). L'analyse a évalué la maturité "
            f"du site pour les moteurs de recherche IA, notamment Google AI Overviews, ChatGPT, Perplexity, "
            f"Gemini et Bing Copilot. Le Score GEO global est de <b>{geo_score}/100</b>, "
            f"ce qui place le site dans le niveau <b>{get_score_label(geo_score)}</b>.",
            styles['BodyText_Custom']
        ))

    elements.append(Spacer(1, 16))

    # ============================================================
    # DÉTAIL DES SCORES
    # ============================================================
    elements.append(Paragraph("Détail du score GEO", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    score_data = [
        ["Composante", "Score", "Pondération", "Score pondéré"],
        ["Citabilité & visibilité IA", f"{ai_citability}/100", "25%", f"{round(ai_citability * 0.25, 1)}"],
        ["Signaux d'autorité de marque", f"{brand_authority}/100", "20%", f"{round(brand_authority * 0.20, 1)}"],
        ["Qualité du contenu & E-E-A-T", f"{content_eeat}/100", "20%", f"{round(content_eeat * 0.20, 1)}"],
        ["Fondations techniques", f"{technical}/100", "15%", f"{round(technical * 0.15, 1)}"],
        ["Données structurées", f"{schema_score}/100", "10%", f"{round(schema_score * 0.10, 1)}"],
        ["Optimisation plateformes", f"{platform_optimization}/100", "10%", f"{round(platform_optimization * 0.10, 1)}"],
        ["TOTAL", f"{geo_score}/100", "100%", f"{geo_score}"],
    ]

    score_table = Table(score_data, colWidths=[200, 80, 60, 80])
    style = make_table_style()

    # Mettre la dernière ligne en gras
    style.add('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold')
    style.add('BACKGROUND', (0, -1), (-1, -1), MEDIUM_BG)

    # Colorier les cellules de score
    for i in range(1, len(score_data) - 1):
        score_val = int(score_data[i][1].split("/")[0])
        color = get_score_color(score_val)
        style.add('TEXTCOLOR', (1, i), (1, i), color)

    score_table.setStyle(style)
    elements.append(score_table)

    elements.append(Spacer(1, 16))

    # Graphique en barres des scores
    chart_scores = [ai_citability, brand_authority, content_eeat, technical, schema_score, platform_optimization]
    chart_labels = ["Citabilité", "Marque", "Contenu", "Technique", "Schémas", "Plateformes"]
    elements.append(create_bar_chart(chart_scores, chart_labels))

    elements.append(PageBreak())

    # ============================================================
    # MATURITÉ PAR PLATEFORME IA
    # ============================================================
    elements.append(Paragraph("Maturité par plateforme IA", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    elements.append(Paragraph(
        "Ces scores reflètent la probabilité que votre contenu soit cité par chaque plateforme de recherche IA. "
        "Un score inférieur à 50 indique des obstacles significatifs à la citation sur cette plateforme.",
        styles['BodyText_Custom']
    ))
    elements.append(Spacer(1, 10))

    # Graphique des plateformes
    if platforms:
        elements.append(create_platform_chart(platforms))

    elements.append(Spacer(1, 10))

    # Tableau des plateformes
    platform_table_data = [["Plateforme IA", "Score", "Niveau"]]
    for name, score in platforms.items():
        status = get_score_label(score)
        platform_table_data.append([name, f"{score}/100", status])

    pt = Table(platform_table_data, colWidths=[180, 80, 150])
    pt_style = make_table_style()
    for i in range(1, len(platform_table_data)):
        score_val = int(platform_table_data[i][1].split("/")[0])
        color = get_score_color(score_val)
        pt_style.add('TEXTCOLOR', (1, i), (1, i), color)
    pt.setStyle(pt_style)
    elements.append(pt)

    elements.append(PageBreak())

    # ============================================================
    # ACCÈS DES ROBOTS IA
    # ============================================================
    elements.append(Paragraph("Statut d'accès des robots IA", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    elements.append(Paragraph(
        "Bloquer les robots IA empêche les plateformes IA de citer votre contenu. "
        "Le tableau ci-dessous indique quels robots IA peuvent actuellement accéder à votre site.",
        styles['BodyText_Custom']
    ))
    elements.append(Spacer(1, 8))

    if crawler_access:
        cell_style = ParagraphStyle(
            'CrawlerCell', fontName='Helvetica', fontSize=9,
            textColor=TEXT_PRIMARY, leading=12,
        )
        header_cell_style = ParagraphStyle(
            'CrawlerHeaderCell', fontName='Helvetica-Bold', fontSize=9,
            textColor=WHITE, leading=12,
        )
        status_style_allowed = ParagraphStyle(
            'StatusAllowed', fontName='Helvetica-Bold', fontSize=9,
            textColor=SUCCESS, leading=12,
        )
        status_style_blocked = ParagraphStyle(
            'StatusBlocked', fontName='Helvetica-Bold', fontSize=9,
            textColor=DANGER, leading=12,
        )
        status_style_restricted = ParagraphStyle(
            'StatusRestricted', fontName='Helvetica-Bold', fontSize=9,
            textColor=WARNING, leading=12,
        )
        status_style_default = ParagraphStyle(
            'StatusDefault', fontName='Helvetica', fontSize=9,
            textColor=TEXT_PRIMARY, leading=12,
        )

        crawler_data = [[
            Paragraph("Robot", header_cell_style),
            Paragraph("Plateforme", header_cell_style),
            Paragraph("Statut", header_cell_style),
            Paragraph("Recommandation", header_cell_style),
        ]]
        for crawler_name, info in crawler_access.items():
            if isinstance(info, dict):
                status_text = info.get("status", "Inconnu")
                status_upper = status_text.upper()
                if "AUTORIS" in status_upper or "ALLOW" in status_upper:
                    s_style = status_style_allowed
                elif "BLOQU" in status_upper or "BLOCK" in status_upper:
                    s_style = status_style_blocked
                elif "RESTREINT" in status_upper or "RESTRICT" in status_upper:
                    s_style = status_style_restricted
                else:
                    s_style = status_style_default

                crawler_data.append([
                    Paragraph(crawler_name, cell_style),
                    Paragraph(info.get("platform", ""), cell_style),
                    Paragraph(status_text, s_style),
                    Paragraph(info.get("recommendation", ""), cell_style),
                ])
            else:
                crawler_data.append([
                    Paragraph(crawler_name, cell_style),
                    Paragraph("", cell_style),
                    Paragraph(str(info), cell_style),
                    Paragraph("", cell_style),
                ])

        ct = Table(crawler_data, colWidths=[90, 110, 72, 240])
        ct_style = make_table_style()
        ct_style.add('VALIGN', (0, 0), (-1, -1), 'TOP')
        ct.setStyle(ct_style)
        elements.append(ct)
    else:
        elements.append(Paragraph(
            "<i>Exécuter /geo crawlers pour alimenter cette section avec les données d'accès des robots IA.</i>",
            styles['BodyText_Custom']
        ))

    elements.append(PageBreak())

    # ============================================================
    # PRINCIPAUX CONSTATS
    # ============================================================
    elements.append(Paragraph("Principaux constats", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    if findings:
        severity_labels = {
            "CRITICAL": "CRITIQUE",
            "HIGH": "IMPORTANT",
            "MEDIUM": "MODÉRÉ",
            "LOW": "FAIBLE",
        }
        for finding in findings:
            severity = finding.get("severity", "info").upper()
            severity_fr = severity_labels.get(severity, severity)
            title = finding.get("title", "")
            description = finding.get("description", "")

            if severity == "CRITICAL":
                sev_color = DANGER
            elif severity == "HIGH":
                sev_color = WARNING
            elif severity == "MEDIUM":
                sev_color = INFO
            else:
                sev_color = TEXT_SECONDARY

            elements.append(Paragraph(
                f'<font color="{sev_color.hexval()}">[{severity_fr}]</font> <b>{title}</b>',
                styles['BodyText_Custom']
            ))
            if description:
                elements.append(Paragraph(description, styles['Recommendation']))
            elements.append(Spacer(1, 4))
    else:
        elements.append(Paragraph(
            "<i>Exécuter un audit /geo complet pour alimenter les constats.</i>",
            styles['BodyText_Custom']
        ))

    elements.append(PageBreak())

    # ============================================================
    # PLAN D'ACTION PRIORISÉ
    # ============================================================
    elements.append(Paragraph("Plan d'action priorisé", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    # Actions rapides
    elements.append(Paragraph("Actions rapides (cette semaine)", styles['SubHeader']))
    elements.append(Paragraph(
        "Impact élevé, effort faible — peuvent être mises en œuvre immédiatement.",
        styles['SmallText']
    ))

    if quick_wins:
        for i, action in enumerate(quick_wins, 1):
            if isinstance(action, dict):
                text = f"<b>{i}.</b> {action.get('action', '')} — <i>{action.get('impact', '')}</i>"
            else:
                text = f"<b>{i}.</b> {action}"
            elements.append(Paragraph(text, styles['Recommendation']))
    else:
        default_wins = [
            "Autoriser tous les robots IA de niveau 1 dans le robots.txt (GPTBot, ClaudeBot, PerplexityBot)",
            "Ajouter la date de publication et de dernière mise à jour à toutes les pages de contenu",
            "Ajouter des signatures d'auteur avec leurs qualifications aux articles et billets de blog",
            "Créer un fichier llms.txt pour guider les systèmes IA vers le contenu clé",
            "Ajouter des propriétés sameAs au schéma Organisation avec les liens vers tous les profils de plateforme",
        ]
        for i, action in enumerate(default_wins, 1):
            elements.append(Paragraph(f"<b>{i}.</b> {action}", styles['Recommendation']))

    elements.append(Spacer(1, 12))

    # Améliorations à moyen terme
    elements.append(Paragraph("Améliorations à moyen terme (ce mois-ci)", styles['SubHeader']))
    elements.append(Paragraph(
        "Impact significatif, effort modéré — nécessite des modifications de contenu ou techniques.",
        styles['SmallText']
    ))

    if medium_term:
        for i, action in enumerate(medium_term, 1):
            if isinstance(action, dict):
                text = f"<b>{i}.</b> {action.get('action', '')} — <i>{action.get('impact', '')}</i>"
            else:
                text = f"<b>{i}.</b> {action}"
            elements.append(Paragraph(text, styles['Recommendation']))
    else:
        default_medium = [
            "Restructurer les 10 pages principales avec des titres sous forme de questions et des réponses directes",
            "Mettre en place un balisage Schema.org complet : Organisation + Article + Personne",
            "Optimiser les blocs de contenu pour la citabilité IA (passages autonomes de 134 à 167 mots)",
            "Assurer le rendu côté serveur pour toutes les pages de contenu public",
            "Implémenter le protocole IndexNow pour accélérer l'indexation Bing/Copilot",
        ]
        for i, action in enumerate(default_medium, 1):
            elements.append(Paragraph(f"<b>{i}.</b> {action}", styles['Recommendation']))

    elements.append(Spacer(1, 12))

    # Initiatives stratégiques
    elements.append(Paragraph("Initiatives stratégiques (ce trimestre)", styles['SubHeader']))
    elements.append(Paragraph(
        "Avantage concurrentiel à long terme — nécessite un investissement continu.",
        styles['SmallText']
    ))

    if strategic:
        for i, action in enumerate(strategic, 1):
            if isinstance(action, dict):
                text = f"<b>{i}.</b> {action.get('action', '')} — <i>{action.get('impact', '')}</i>"
            else:
                text = f"<b>{i}.</b> {action}"
            elements.append(Paragraph(text, styles['Recommendation']))
    else:
        default_strategic = [
            "Construire une présence sur Wikipedia/Wikidata grâce à des articles de presse et la notoriété",
            "Développer une stratégie d'engagement actif sur Reddit dans les sous-forums pertinents",
            "Créer une stratégie de contenu YouTube alignée sur les requêtes de recherche IA",
            "Établir un programme de publication de données et recherches originales pour une citabilité unique",
            "Construire une autorité thématique via des clusters de contenu complets",
        ]
        for i, action in enumerate(default_strategic, 1):
            elements.append(Paragraph(f"<b>{i}.</b> {action}", styles['Recommendation']))

    elements.append(PageBreak())

    # ============================================================
    # MÉTHODOLOGIE & GLOSSAIRE
    # ============================================================
    elements.append(Paragraph("Annexe : Méthodologie", styles['SectionHeader']))
    elements.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    elements.append(Paragraph(
        f"Cet audit GEO a été conduit le {date} sur {url}. "
        "L'analyse a évalué le site selon six dimensions : Citabilité & visibilité IA (25%), "
        "Signaux d'autorité de marque (20%), Qualité du contenu & E-E-A-T (20%), Fondations techniques (15%), "
        "Données structurées (10%) et Optimisation des plateformes (10%).",
        styles['BodyText_Custom']
    ))

    elements.append(Spacer(1, 8))

    elements.append(Paragraph(
        "<b>Plateformes évaluées :</b> Google AI Overviews, ChatGPT Web Search, Perplexity AI, "
        "Google Gemini, Bing Copilot",
        styles['BodyText_Custom']
    ))

    elements.append(Paragraph(
        "<b>Standards de référence :</b> Directives d'évaluation de la qualité de la recherche Google (déc. 2025), "
        "spécification Schema.org, Core Web Vitals (seuils 2026), "
        "standard émergent llms.txt, cadre de licence RSL 1.0",
        styles['BodyText_Custom']
    ))

    elements.append(Spacer(1, 16))

    # Glossaire
    elements.append(Paragraph("Glossaire", styles['SubHeader']))

    glossary = [
        ["Terme", "Définition"],
        ["GEO", "Generative Engine Optimization — optimisation du contenu pour être cité par les plateformes de recherche IA"],
        ["AIO", "AI Overviews — encarts de réponses IA de Google en haut des résultats de recherche"],
        ["E-E-A-T", "Expérience, Expertise, Autorité, Fiabilité — cadre de qualité du contenu de Google"],
        ["SSR", "Server-Side Rendering — génération du HTML côté serveur pour que les robots puissent lire le contenu sans JavaScript"],
        ["CWV", "Core Web Vitals — métriques d'expérience de page de Google (LCP, INP, CLS)"],
        ["INP", "Interaction to Next Paint — métrique de réactivité (remplace FID depuis mars 2024)"],
        ["JSON-LD", "JavaScript Object Notation for Linked Data — format de données structurées recommandé"],
        ["sameAs", "Propriété Schema.org reliant une entité à ses profils sur d'autres plateformes"],
        ["llms.txt", "Fichier standard proposé pour guider les systèmes IA sur le contenu d'un site"],
        ["IndexNow", "Protocole de notification instantanée aux moteurs de recherche lors de modifications de contenu"],
    ]

    gt = Table(glossary, colWidths=[80, 380])
    gt.setStyle(make_table_style())
    elements.append(gt)

    elements.append(Spacer(1, 30))

    # Mention de bas de page
    elements.append(HRFlowable(width="100%", thickness=0.5, color=lightgrey, spaceAfter=8))
    elements.append(Paragraph(
        "Ce rapport a été généré par l'outil d'analyse GEO-SEO Claude Code. "
        "Les scores et recommandations sont basés sur une analyse automatisée et des benchmarks sectoriels. "
        "Les résultats doivent être validés par des tests spécifiques à chaque plateforme.",
        styles['SmallText']
    ))

    # ============================================================
    # GÉNÉRATION DU PDF
    # ============================================================
    doc.build(elements, onFirstPage=header_footer, onLaterPages=header_footer)
    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Générer un rapport exemple pour démonstration
        sample_data = {
            "url": "https://exemple.com",
            "brand_name": "Exemple Entreprise",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "geo_score": 58,
            "scores": {
                "ai_citability": 45,
                "brand_authority": 62,
                "content_eeat": 70,
                "technical": 55,
                "schema": 30,
                "platform_optimization": 48,
            },
            "platforms": {
                "Google AI Overviews": 65,
                "ChatGPT": 52,
                "Perplexity": 48,
                "Gemini": 60,
                "Bing Copilot": 45,
            },
            "executive_summary": (
                "Ce rapport présente les résultats d'un audit GEO complet "
                "conduit sur Exemple Entreprise (https://exemple.com). Le site a obtenu "
                "un Score GEO global de 58/100, le plaçant dans le niveau Moyen. "
                "Le point le plus fort est la qualité du contenu (70/100), tandis que les données "
                "structurées (30/100) représentent la principale opportunité d'amélioration. "
                "La mise en place des schémas, l'autorisation des robots IA et l'optimisation "
                "de la structure du contenu pourraient porter le score à environ 78/100 sous 90 jours."
            ),
            "findings": [
                {"severity": "critical", "title": "Aucun balisage de données structurées détecté",
                 "description": "Le site ne comporte aucune donnée structurée JSON-LD, ce qui rend difficile pour les modèles IA de comprendre les relations entre entités."},
                {"severity": "high", "title": "Rendu JavaScript uniquement",
                 "description": "Les pages de contenu clés utilisent le rendu côté client, les rendant invisibles pour les robots IA qui n'exécutent pas JavaScript."},
                {"severity": "high", "title": "Fichier llms.txt absent",
                 "description": "Aucun fichier llms.txt n'existe pour guider les systèmes IA vers le contenu le plus important."},
                {"severity": "medium", "title": "Présence d'entité de marque insuffisante",
                 "description": "La marque n'est pas présente sur Wikipedia ni Wikidata, ce qui limite la reconnaissance de l'entité par les modèles IA."},
                {"severity": "medium", "title": "Contenu non optimisé pour la citabilité",
                 "description": "La plupart des blocs de contenu sont soit trop courts soit trop longs pour une citation IA optimale (cible : 134 à 167 mots)."},
            ],
            "quick_wins": [
                "Autoriser tous les robots IA de niveau 1 dans le robots.txt",
                "Ajouter les dates de publication à toutes les pages de contenu",
                "Créer un fichier llms.txt avec les références des pages clés",
                "Ajouter des signatures d'auteur avec leurs qualifications",
                "Corriger les meta descriptions sur les 10 pages principales",
            ],
            "medium_term": [
                "Mettre en place le schéma Organisation avec les liens sameAs",
                "Ajouter les schémas Article + Personne à tous les articles de blog",
                "Restructurer le contenu avec des titres H2 sous forme de questions",
                "Optimiser les blocs de contenu pour une citabilité de 134 à 167 mots",
                "Implémenter le rendu côté serveur pour les pages de contenu",
            ],
            "strategic": [
                "Construire une présence sur Wikipedia/Wikidata",
                "Développer une stratégie d'engagement sur Reddit",
                "Créer du contenu YouTube aligné sur les requêtes de recherche IA",
                "Établir un programme de publication de recherches originales",
                "Construire des clusters de contenu thématique complets",
            ],
            "crawler_access": {
                "GPTBot": {"platform": "ChatGPT", "status": "Autorisé", "recommendation": "Maintenir l'accès"},
                "ClaudeBot": {"platform": "Claude", "status": "Autorisé", "recommendation": "Maintenir l'accès"},
                "PerplexityBot": {"platform": "Perplexity", "status": "Bloqué", "recommendation": "Débloquer pour améliorer la visibilité"},
                "Google-Extended": {"platform": "Gemini", "status": "Autorisé", "recommendation": "Maintenir l'accès"},
                "Bingbot": {"platform": "Bing Copilot", "status": "Autorisé", "recommendation": "Maintenir l'accès"},
            },
        }

        output_file = "GEO-RAPPORT-exemple.pdf"
        result = generate_report(sample_data, output_file)
        print(f"Rapport généré : {result}")

    else:
        # Charger les données depuis un fichier ou stdin
        input_path = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "GEO-RAPPORT.pdf"

        if input_path == "-":
            data = json.loads(sys.stdin.read())
        else:
            with open(input_path) as f:
                data = json.load(f)

        result = generate_report(data, output_file)
        print(f"Rapport généré : {result}")
