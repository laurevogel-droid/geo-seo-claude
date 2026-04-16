---
name: geo-report
description: Générer un rapport GEO professionnel à destination du client, combinant tous les résultats d'audit en un livrable unique avec scores, constats et plan d'action priorisé
version: 1.0.0
author: geo-seo-claude
tags: [geo, report, client-deliverable, executive-summary, action-plan]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Générateur de rapport GEO client

## Objectif

Cette compétence agrège les résultats de toutes les compétences d'audit GEO en un rapport unique et professionnel, livrable directement à un client ou à une direction. Le rapport est rédigé pour **les dirigeants et responsables marketing**, pas pour des développeurs — les constats techniques sont traduits en impact business et en actions concrètes priorisées.

## Comment utiliser cette compétence

1. Exécuter les audits suivants au préalable (ou utiliser des données de rapport existantes) :
   - `geo-platform-optimizer` -> GEO-PLATFORM-OPTIMIZATION.md
   - `geo-schema` -> GEO-SCHEMA-REPORT.md
   - `geo-technical` -> GEO-TECHNICAL-AUDIT.md
   - `geo-content` -> GEO-CONTENT-ANALYSIS.md
   - (Optionnel) `geo-llms-txt` -> évaluation llms.txt
   - (Optionnel) `geo-brand-mentions` -> données d'autorité de marque
2. Collecter tous les scores et constats
3. Calculer le score GEO composite
4. Générer le rapport client en utilisant le modèle ci-dessous
5. Livrable : GEO-CLIENT-REPORT.md

---

## Calcul du Score GEO

### Pondération des composantes

| Composante | Pondération | Compétence source |
|---|---|---|
| Visibilité sur les plateformes IA | 25% | geo-platform-optimizer |
| Qualité du contenu & E-E-A-T | 25% | geo-content |
| Fondations techniques | 20% | geo-technical |
| Schémas & données structurées | 15% | geo-schema |
| Autorité de marque & présence d'entité | 15% | geo-platform-optimizer (signaux d'entité) |

### Formule de calcul

```
Score GEO = (Score Plateformes × 0,25) + (Score Contenu × 0,25) + (Score Technique × 0,20) + (Score Schémas × 0,15) + (Score Marque × 0,15)
```

Arrondir à l'entier le plus proche. Plafonner à 100.

### Interprétation du score pour les clients

| Plage de score | Niveau | Description client |
|---|---|---|
| 85-100 | Excellent | Votre site est bien positionné pour la recherche IA. Concentrez-vous sur le maintien et l'extension de votre avance. |
| 70-84 | Bon | Bases solides avec des opportunités claires d'amélioration de la visibilité IA. Des optimisations ciblées produiront des résultats significatifs. |
| 55-69 | Moyen | Votre site présente des lacunes en matière de maturité IA que vos concurrents exploitent peut-être déjà. Un plan d'optimisation structuré comblera ces écarts. |
| 40-54 | Insuffisant | Des obstacles significatifs à la visibilité dans la recherche IA existent. Sans action, votre marque risque d'être invisible dans les réponses générées par l'IA. |
| 0-39 | Critique | Des problèmes critiques de maturité IA nécessitent une action immédiate. Vos concurrents captent probablement le trafic de recherche IA qui devrait vous revenir. |

---

## Modèle de rapport

Le rapport complet suit cette structure exacte. Chaque section comprend des instructions sur ce qu'il faut rédiger et comment.

---

### Section 1 : Synthèse exécutive

Rédiger exactement UN paragraphe (4 à 6 phrases) couvrant :
- Ce qui a été analysé (domaine, nombre de pages, date d'analyse)
- Le Score GEO global avec contexte (« XX/100, ce qui place [marque] dans le niveau [niveau] »)
- Le constat le plus impactant (positif ou négatif)
- Les 3 recommandations prioritaires en une phrase
- Une phrase sur l'impact business (« Traiter ces recommandations pourrait augmenter le trafic généré par l'IA d'environ XX%, représentant approximativement X XXX €/mois selon les tendances de trafic actuelles »)

**Ton** : Confiant, direct, professionnel. Pas de jargon. Pas de formulations hésitantes. Rédigez comme un consultant qui présente ses conclusions, pas comme un outil qui génère un rapport.

### Section 2 : Score GEO

Présenter le score global de manière visible :

```
## Score GEO : XX/100 — [Niveau]
```

Puis détailler par composante dans un tableau :

```markdown
| Composante | Score | Pondération | Score pondéré |
|---|---|---|---|
| Visibilité sur les plateformes IA | XX/100 | 25% | XX |
| Qualité du contenu & E-E-A-T | XX/100 | 25% | XX |
| Fondations techniques | XX/100 | 20% | XX |
| Schémas & données structurées | XX/100 | 15% | XX |
| Autorité de marque | XX/100 | 15% | XX |
| **Total** | | | **XX/100** |
```

### Section 3 : Tableau de bord de visibilité IA

Présenter les scores de maturité par plateforme :

```markdown
## Tableau de bord de visibilité IA

| Plateforme IA | Score de maturité | Lacune principale | Action prioritaire |
|---|---|---|---|
| Google AI Overviews | XX/100 | [Lacune en une ligne] | [Action en une ligne] |
| ChatGPT Web Search | XX/100 | [Lacune en une ligne] | [Action en une ligne] |
| Perplexity AI | XX/100 | [Lacune en une ligne] | [Action en une ligne] |
| Google Gemini | XX/100 | [Lacune en une ligne] | [Action en une ligne] |
| Bing Copilot | XX/100 | [Lacune en une ligne] | [Action en une ligne] |
```

Ajouter un court paragraphe expliquant la signification de ces scores : « Ces scores reflètent la probabilité que votre contenu soit cité par chaque plateforme de recherche IA. Un score inférieur à 50 indique des obstacles significatifs à la citation sur cette plateforme. »

### Section 4 : Accès des robots d'indexation IA

Présenter sous forme de tableau clair :

```markdown
## Accès des robots IA

| Robot IA | Plateforme | Statut | Impact | Recommandation |
|---|---|---|---|---|
| Googlebot | Google Search + AIO | Autorisé/Bloqué | Critique | [Action] |
| GPTBot | ChatGPT / OpenAI | Autorisé/Bloqué | Élevé | [Action] |
| Bingbot | Bing + Copilot + ChatGPT | Autorisé/Bloqué | Élevé | [Action] |
| PerplexityBot | Perplexity AI | Autorisé/Bloqué | Moyen | [Action] |
| Google-Extended | Gemini Training | Autorisé/Bloqué | Moyen | [Action] |
| ClaudeBot | Anthropic Claude | Autorisé/Bloqué | Moyen | [Action] |
| Applebot-Extended | Apple Intelligence | Autorisé/Bloqué | Moyen | [Action] |
```

**Traduction pour le client** : « Bloquer les robots IA revient à fermer votre commerce aux heures d'ouverture. Si un robot ne peut pas accéder à votre site, la plateforme IA qu'il alimente ne peut pas citer votre contenu. Nous recommandons d'autoriser tous les principaux robots IA, sauf en cas de préoccupation spécifique liée aux licences de données. »

### Section 5 : Analyse de l'autorité de marque

Présenter la présence de l'entité sur les différentes plateformes :

```markdown
## Autorité de marque

| Plateforme | Présence | Statut | Impact sur la visibilité IA |
|---|---|---|---|
| Wikipedia | Oui/Non | [Détail] | Très élevé — 47,9% des citations ChatGPT proviennent de Wikipedia |
| Wikidata | Oui/Non | [Détail] | Élevé — données d'entité lisibles par les machines |
| LinkedIn | Oui/Non | [Détail] | Élevé — signal Bing Copilot et ChatGPT |
| YouTube | Oui/Non | [Détail] | Élevé — signal Gemini et Perplexity |
| Reddit | Oui/Non | [Détail] | Très élevé — 46,7% des citations Perplexity proviennent de Reddit |
| Google Knowledge Panel | Oui/Non | [Détail] | Élevé — reconnaissance d'entité Gemini |
| Crunchbase | Oui/Non | [Détail] | Moyen — validation d'entité |
| GitHub | Oui/Non | [Détail] | Moyen — signal de marque tech |
```

**Traduction pour le client** : « Les plateformes IA construisent la confiance en recoupant votre marque sur plusieurs sources faisant autorité. Chaque plateforme où votre marque dispose d'une présence exacte et cohérente augmente la probabilité d'être citée dans les réponses IA. »

### Section 6 : Analyse de la citabilité

#### Les 5 pages les plus citables
Pour chaque page :
- URL
- Pourquoi elle est citable (structure, profondeur, signaux E-E-A-T)
- Une amélioration spécifique qui la rendrait encore plus citable

#### Les 5 pages les moins citables
Pour chaque page :
- URL
- Pourquoi elle a peu de chances d'être citée (contenu insuffisant, structure médiocre, signaux manquants)
- Recommandation spécifique de réécriture ou de restructuration

**Cadrage de l'impact business** : « Vos pages les plus citables sont vos meilleures candidates pour apparaître dans les réponses générées par l'IA. Améliorer les 5 pages les moins citables représente l'investissement contenu au meilleur ROI pour la visibilité IA. »

### Section 7 : Synthèse de la santé technique

Présenter les principaux constats techniques dans un langage accessible aux décideurs :

```markdown
## Santé technique

| Domaine | Statut | Impact business |
|---|---|---|
| Core Web Vitals | Bon/À améliorer/Médiocre | [Impact sur l'expérience utilisateur et le classement] |
| Rendu côté serveur (SSR) | Oui/Partiel/Non | [Impact sur la visibilité auprès des robots IA] |
| Optimisation mobile | Bon/À améliorer/Médiocre | [Impact sur l'indexation mobile-first de Google] |
| Sécurité (HTTPS + en-têtes) | Bon/À améliorer/Médiocre | [Impact sur les signaux de confiance] |
| Vitesse de chargement | Rapide/Moyen/Lent | [Impact sur l'expérience utilisateur et le budget de crawl] |
| Protocole IndexNow | Implémenté/Absent | [Impact sur la vitesse d'indexation Bing/ChatGPT] |
```

**Mise en avant du constat critique** : Si le SSR est absent ou partiel, le signaler de manière visible : « Votre site utilise le rendu côté client, ce qui signifie que les robots IA voient une page vide lorsqu'ils le visitent. C'est le problème technique le plus impactant pour la visibilité dans la recherche IA. Tant que ce point n'est pas résolu, la plupart des plateformes IA ne peuvent pas citer votre contenu. »

### Section 8 : Schémas & données structurées

```markdown
## Schémas & données structurées

### Implémentation actuelle
| Type de schéma | Présent | Statut | Impact IA |
|---|---|---|---|
| Organisation | Oui/Non | [Valide/Problèmes] | Critique — reconnaissance d'entité |
| Article + Auteur | Oui/Non | [Valide/Problèmes] | Élevé — signal E-E-A-T |
| sameAs (liens d'entité) | Oui/Non | [Nombre] liens | Critique — graphe d'entité multi-plateformes |
| [Spécifique au secteur] | Oui/Non | [Valide/Problèmes] | [Impact] |
| WebSite + SearchAction | Oui/Non | [Valide/Problèmes] | Moyen — liens annexes |
| BreadcrumbList | Oui/Non | [Valide/Problèmes] | Faible à moyen — contexte de navigation |
```

Si des schémas sont manquants, indiquer : « Le code de données structurées prêt à l'emploi a été préparé et est inclus en annexe technique. Votre équipe de développement peut l'ajouter au site avec un effort minimal. »

### Section 9 : Statut du llms.txt

```markdown
## llms.txt — Guide de contenu pour les IA

| Fichier | Statut | Recommandation |
|---|---|---|
| /llms.txt | Présent/Absent | [Action] |
| /llms-full.txt | Présent/Absent | [Action] |
```

**Traduction pour le client** : « Le llms.txt est un standard émergent (similaire au robots.txt) qui indique aux systèmes IA le contenu de votre site et les pages les plus importantes. S'il n'est pas encore universellement adopté, sa mise en place positionne votre marque en avance sur vos concurrents et fournit des instructions directes aux plateformes IA. »

### Section 10 : Plan d'action priorisé

C'est la section la plus importante du rapport. Organiser les actions par horizon temporel et par impact.

```markdown
## Plan d'action priorisé

### Actions rapides (cette semaine)
*Impact élevé, effort faible — peuvent être mises en œuvre immédiatement*

| N° | Action | Impact | Effort | Plateformes concernées |
|---|---|---|---|---|
| 1 | [Action spécifique] | [Élevé/Moyen] | [Estimation en heures] | [Quelles plateformes IA] |
| 2 | [Action spécifique] | [Élevé/Moyen] | [Estimation en heures] | [Quelles plateformes IA] |
```

**Critères des actions rapides** : Réalisables en moins de 4 heures par une seule personne. Exemples :
- Autoriser les robots IA dans le robots.txt
- Ajouter des dates de publication aux contenus existants
- Ajouter des signatures d'auteur avec leurs qualifications
- Corriger les meta descriptions manquantes ou incorrectes
- Ajouter des propriétés sameAs au schéma Organisation existant
- Créer/revendiquer le fichier llms.txt

```markdown
### Améliorations à moyen terme (ce mois-ci)
*Impact significatif, effort modéré — nécessite des modifications de contenu ou techniques*

| N° | Action | Impact | Effort | Plateformes concernées |
|---|---|---|---|---|
| 1 | [Action spécifique] | [Élevé/Moyen] | [Estimation en jours] | [Quelles plateformes IA] |
```

**Critères moyen terme** : 1 à 5 jours de travail. Exemples :
- Restructurer les 10 pages principales avec des titres sous forme de questions et des réponses directes
- Mettre en place un balisage Schema.org complet
- Créer des pages d'auteur avec qualifications et liens sameAs
- Optimiser les Core Web Vitals (compression d'images, découpage du code)
- S'inscrire et configurer Bing Webmaster Tools
- Implémenter le protocole IndexNow

```markdown
### Initiatives stratégiques (ce trimestre)
*Avantage concurrentiel à long terme, nécessite un investissement continu*

| N° | Action | Impact | Effort | Plateformes concernées |
|---|---|---|---|---|
| 1 | [Action spécifique] | [Élevé/Moyen] | [Estimation en semaines] | [Quelles plateformes IA] |
```

**Critères stratégiques** : Effort continu sur plusieurs semaines ou mois. Exemples :
- Construire une présence sur Wikipedia/Wikidata
- Développer une stratégie d'engagement sur Reddit
- Créer une stratégie de contenu YouTube alignée sur les requêtes de recherche
- Implémenter le rendu côté serveur (si actuellement rendu côté client)
- Construire une autorité thématique via une stratégie de contenu complète
- Établir un programme de publication de données et recherches originales

### Impact estimé
Après le plan d'action, inclure une estimation d'impact :

« Sur la base des benchmarks sectoriels et des lacunes spécifiques identifiées dans cet audit :
- **Les actions rapides seules** pourraient améliorer votre score GEO d'environ [X à Y] points
- **La mise en œuvre complète** de ce plan d'action pourrait porter votre score GEO à environ [XX]/100
- Aux niveaux de trafic et de taux de conversion actuels, l'amélioration de la visibilité IA représente une valeur organique additionnelle estimée à **X XXX € - XX XXX € par mois** »

Utiliser des estimations conservatrices. Énoncer clairement les hypothèses. Ne jamais garantir des résultats spécifiques.

### Section 11 : Comparaison concurrentielle (si des URL concurrentes ont été fournies)

Si des URL concurrentes ont été analysées en parallèle du domaine principal :

```markdown
## Comparaison concurrentielle

| Indicateur | [Votre marque] | [Concurrent 1] | [Concurrent 2] |
|---|---|---|---|
| Score GEO global | XX/100 | XX/100 | XX/100 |
| Maturité Google AIO | XX/100 | XX/100 | XX/100 |
| Maturité ChatGPT | XX/100 | XX/100 | XX/100 |
| Maturité Perplexity | XX/100 | XX/100 | XX/100 |
| Couverture des schémas | [Détail] | [Détail] | [Détail] |
| Présence Wikipedia | Oui/Non | Oui/Non | Oui/Non |
| Autorité Reddit | [Détail] | [Détail] | [Détail] |
| Statut SSR | Oui/Non | Oui/Non | Oui/Non |

### Vos points forts
[Domaines spécifiques où la marque surpasse ses concurrents]

### Vos points de retard
[Domaines spécifiques où les concurrents ont un avantage, avec les actions pour combler l'écart]
```

### Section 12 : Annexe

```markdown
## Annexe

### Méthodologie
Cet audit GEO a été conduit selon la méthodologie suivante :
- **Pages analysées** : [Liste des URL spécifiques auditées]
- **Plateformes évaluées** : Google AI Overviews, ChatGPT, Perplexity AI, Google Gemini, Bing Copilot
- **Vérifications techniques** : en-têtes HTTP, robots.txt, analyse du code source HTML, validation des données structurées
- **Évaluation du contenu** : cadre E-E-A-T (Expérience, Expertise, Autorité, Fiabilité) selon les Directives d'évaluation de la qualité de Google (mise à jour de décembre 2025)
- **Validation des schémas** : analyse JSON-LD et conformité à la spécification Schema.org
- **Date d'analyse** : [Date]

### Sources de données
- Directives d'évaluation de la qualité de la recherche Google (mise à jour décembre 2025)
- Hiérarchie complète des types Schema.org
- Études sectorielles sur les citations (Zyppy, Authoritas, recherches Semrush sur la recherche IA, 2025-2026)
- Seuils Core Web Vitals (web.dev, standards 2026)
- Documentation officielle des agents utilisateurs des robots IA (par plateforme)

### Glossaire

| Terme | Définition |
|---|---|
| GEO | Generative Engine Optimization — optimisation du contenu pour être cité par les plateformes de recherche IA |
| AIO | AI Overviews — encarts de réponses IA de Google en haut des résultats de recherche |
| E-E-A-T | Expérience, Expertise, Autorité, Fiabilité — cadre de qualité du contenu de Google |
| SSR | Server-Side Rendering (Rendu côté serveur) — génération du HTML côté serveur pour que les robots puissent lire le contenu sans JavaScript |
| CWV | Core Web Vitals — métriques d'expérience de page de Google (LCP, INP, CLS) |
| LCP | Largest Contentful Paint — temps de rendu du plus grand élément visible |
| INP | Interaction to Next Paint — métrique de réactivité (remplace FID depuis mars 2024) |
| CLS | Cumulative Layout Shift — métrique de stabilité visuelle |
| JSON-LD | JavaScript Object Notation for Linked Data — format de données structurées recommandé |
| sameAs | Propriété Schema.org reliant une entité à ses profils sur d'autres plateformes |
| IndexNow | Protocole de notification instantanée aux moteurs de recherche lors de modifications de contenu |
| llms.txt | Fichier standard proposé pour guider les systèmes IA sur le contenu d'un site |
| YMYL | Your Money or Your Life — sujets nécessitant les standards E-E-A-T les plus élevés |
| SERP | Search Engine Results Page — page de résultats des moteurs de recherche |
| Autorité thématique | Profondeur et étendue de la couverture d'un site sur son domaine principal |
```

---

## Directives de mise en forme et de ton

### Mise en forme
- Utiliser du markdown propre tout au long du rapport : tableaux, titres (H2/H3), listes à puces, gras pour les points clés
- Tableaux pour les données, listes pour les recommandations, gras pour les termes essentiels
- Une ligne vide entre les sections pour la lisibilité
- Utiliser des séparateurs horizontaux (---) entre les grandes sections
- Toutes les URL doivent être absolues (pas relatives)

### Ton
- **Professionnel mais accessible** — rédigé pour un dirigeant d'entreprise, pas pour un développeur
- **Confiant et direct** — énoncer les constats comme des conclusions, pas des possibilités
- **Orienté action** — chaque constat doit être relié à une action spécifique
- **Centré sur l'impact business** — traduire les problèmes techniques en résultats business
- À éviter : jargon sans explication, formulations hésitantes, voix passive, mises en garde excessives
- À utiliser : « Votre site [fait/ne fait pas]... », « Nous recommandons... », « Cela impacte... »

### Valorisation en euros
Lorsque c'est possible, relier les recommandations à la valeur business :
- « Améliorer votre maturité Google AIO de 35 à 70 pourrait augmenter votre présence dans les AI Overviews d'environ 50%, ce qui aux volumes de recherche actuels représente environ 2 000 visiteurs mensuels supplémentaires »
- « Le rendu côté serveur rendrait votre contenu accessible à ChatGPT, Perplexity et d'autres plateformes IA — un public que vos concurrents atteignent déjà »
- « L'investissement dans le balisage Schema.org (estimé à 8 à 16 heures de travail développeur) pourrait faire passer votre score de reconnaissance d'entité de 20 à 75, améliorant significativement la probabilité de citation »

Utiliser des estimations conservatrices. Énoncer clairement les hypothèses. Ne jamais garantir des résultats spécifiques.

---

## Livrable

Générer **GEO-CLIENT-REPORT.md** en utilisant le modèle complet ci-dessus, renseigné avec les données réelles de l'audit. Le rapport doit être :
- Équivalent à 40-80 pages en termes de détail (3 000 à 6 000 mots)
- Prêt à être envoyé à un client sans modification
- Autonome (sans référence à d'autres fichiers de rapport — toutes les données pertinentes sont incluses)
- Imprimable et présentable (mise en forme markdown propre)
