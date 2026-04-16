---
name: geo-report-pdf
description: Générer un rapport PDF professionnel à partir des données d'audit GEO avec ReportLab. Produit un PDF soigné et prêt pour le client avec jauges de score, graphiques en barres, visualisations de maturité par plateforme, tableaux en couleur et plan d'action priorisé.
version: 1.0.0
author: geo-seo-claude
tags: [geo, pdf, report, client-deliverable, professional]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Générateur de rapport GEO au format PDF

## Objectif

Cette compétence génère un rapport PDF professionnel et visuellement soigné à partir des données d'audit GEO. Le PDF inclut des jauges de score, des graphiques en barres, des visualisations de maturité par plateforme IA, des tableaux en couleur et un plan d'action priorisé — prêt à être livré directement aux clients.

## Prérequis

- **ReportLab** doit être installé : `pip install reportlab`
- Le script de génération PDF se trouve à : `~/.claude/skills/geo/scripts/generate_pdf_report.py`
- Exécuter un audit GEO complet au préalable (via `/geo-audit`) afin de disposer des données à inclure dans le rapport

## Comment générer un rapport PDF

### Étape 1 : Collecter les données d'audit

Après avoir exécuté un `/geo-audit` complet, rassembler tous les scores, constats et recommandations dans une structure JSON. Les données JSON doivent respecter ce schéma :

```json
{
    "url": "https://exemple.com",
    "brand_name": "Nom de l'entreprise",
    "date": "2026-02-18",
    "geo_score": 65,
    "scores": {
        "ai_citability": 62,
        "brand_authority": 78,
        "content_eeat": 74,
        "technical": 72,
        "schema": 45,
        "platform_optimization": 59
    },
    "platforms": {
        "Google AI Overviews": 68,
        "ChatGPT": 62,
        "Perplexity": 55,
        "Gemini": 60,
        "Bing Copilot": 50
    },
    "executive_summary": "Synthèse en 4 à 6 phrases des principaux constats de l'audit...",
    "findings": [
        {
            "severity": "critical",
            "title": "Titre du constat",
            "description": "Description du constat et de son impact."
        }
    ],
    "quick_wins": [
        "Action prioritaire 1",
        "Action prioritaire 2"
    ],
    "medium_term": [
        "Action moyen terme 1",
        "Action moyen terme 2"
    ],
    "strategic": [
        "Initiative stratégique 1",
        "Initiative stratégique 2"
    ],
    "crawler_access": {
        "GPTBot": {"platform": "ChatGPT", "status": "Autorisé", "recommendation": "Maintenir l'accès"},
        "ClaudeBot": {"platform": "Claude", "status": "Bloqué", "recommendation": "Débloquer pour améliorer la visibilité"}
    }
}
```

### Étape 2 : Écrire les données JSON dans un fichier temporaire

Écrire les données d'audit collectées dans un fichier JSON temporaire :

```bash
# Écriture des données d'audit dans un fichier temporaire
cat > /tmp/geo-audit-data.json << 'EOF'
{ ... données JSON de l'audit ... }
EOF
```

### Étape 3 : Générer le PDF

Exécuter le script de génération PDF :

```bash
python3 ~/.claude/skills/geo/scripts/generate_pdf_report.py /tmp/geo-audit-data.json GEO-RAPPORT-[marque].pdf
```

Le script produira un rapport PDF professionnel comprenant :
- **Page de couverture** — Nom de la marque, URL, date, score GEO global avec jauge visuelle
- **Synthèse exécutive** — Principaux constats et recommandations prioritaires
- **Détail des scores** — Tableau et graphique en barres des 6 catégories de notation
- **Maturité par plateforme IA** — Graphique horizontal par plateforme avec scores
- **Accès des robots IA** — Tableau en couleur (vert = autorisé, rouge = bloqué)
- **Principaux constats** — Liste des constats classés par sévérité (critique/élevé/moyen/faible)
- **Plan d'action priorisé** — Actions rapides, moyen terme et initiatives stratégiques
- **Annexe** — Méthodologie, sources de données et glossaire

### Étape 4 : Retourner le chemin du PDF

Après la génération, indiquer à l'utilisateur l'emplacement du PDF et sa taille.

## Exemple de workflow complet

Lors de l'exécution de cette compétence, suivre cette séquence exacte :

1. **Vérifier l'existence de données d'audit** — Rechercher les rapports d'audit GEO récents dans le répertoire courant :
   - `GEO-CLIENT-REPORT.md`
   - `GEO-AUDIT-REPORT.md`
   - Ou tout fichier `GEO-*.md` issu d'un audit récent

2. **Si aucune donnée d'audit n'existe** — Demander à l'utilisateur d'exécuter `/geo-audit <url>` en premier, puis de revenir pour générer le PDF.

3. **Si des données d'audit existent** — Analyser le rapport markdown pour en extraire :
   - Le score GEO global
   - Les scores par catégorie (citabilité, autorité de marque, contenu/E-E-A-T, technique, schémas, plateformes)
   - Les scores de maturité par plateforme (Google AIO, ChatGPT, Perplexity, Gemini, Bing Copilot)
   - Le statut d'accès des robots IA
   - Les principaux constats avec leurs niveaux de sévérité
   - Les actions rapides, moyen terme et initiatives stratégiques
   - La synthèse exécutive

4. **Construire le JSON** — Structurer toutes les données selon le schéma JSON présenté ci-dessus.

5. **Écrire le JSON dans un fichier temporaire** — Sauvegarder dans `/tmp/geo-audit-data.json`

6. **Exécuter le générateur PDF** :
   ```bash
   python3 ~/.claude/skills/geo/scripts/generate_pdf_report.py /tmp/geo-audit-data.json "GEO-RAPPORT-[nom_marque].pdf"
   ```

7. **Confirmer la réussite** — Indiquer à l'utilisateur que le PDF a été généré, son emplacement et sa taille.

## Si l'utilisateur fournit une URL

Si l'utilisateur exécute `/geo-report-pdf https://exemple.com` avec une URL :
1. Lancer d'abord un audit complet : invoquer la compétence `geo-audit` pour cette URL
2. Collecter ensuite toutes les données d'audit depuis les fichiers de rapport générés
3. Générer le PDF comme décrit ci-dessus

## Extraction des données depuis un rapport markdown

Lors de l'extraction de données depuis des rapports GEO au format markdown, rechercher ces patterns :

- **Score GEO** : Rechercher « Score GEO : XX/100 » ou « Total : XX/100 » ou « Score GEO : XX »
- **Scores par catégorie** : Rechercher des tableaux avec des colonnes du type « Composante | Score | Pondération »
- **Scores par plateforme** : Rechercher des tableaux mentionnant « Google AI Overviews », « ChatGPT », « Perplexity », etc.
- **Statut des robots** : Rechercher des tableaux avec les statuts « Autorisé » ou « Bloqué » pour des robots comme GPTBot, ClaudeBot
- **Constats** : Rechercher les sections intitulées « Principaux constats », « Problèmes critiques », « Recommandations »
- **Actions** : Rechercher les sections intitulées « Actions rapides », « Plan d'action », « Recommandations »

## Notes

- Si ReportLab n'est pas installé, exécuter : `pip install reportlab`
- Le PDF est conçu au format Lettre US (8,5" x 11")
- Palette de couleurs : bleu marine principal (#1a1a2e), accent bleu (#0f3460), accent corail (#e94560), vert succès (#00b894)
- Chaque page comporte un filet d'en-tête, une numérotation des pages, un filigrane « Confidentiel » et la date de génération
- Les jauges de score utilisent les couleurs du feu tricolore : vert (80+), bleu (60-79), jaune (40-59), rouge (moins de 40)
