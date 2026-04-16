---
name: geo-platform-optimizer
description: Platform-specific AI search optimization — audit and optimize for Google AI Overviews, ChatGPT, Perplexity, Gemini, and Bing Copilot individually
version: 1.0.0
author: geo-seo-claude
tags: [geo, ai-search, platform-optimization, chatgpt, perplexity, gemini, aio]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# GEO Platform Optimizer

## Core Insight

Only **11% of domains** are cited by BOTH ChatGPT and Google AI Overviews for the same query. Each AI search platform uses different indexes, ranking logic, and source preferences. A page optimized for Google AI Overviews may be invisible to ChatGPT, and vice versa. Platform-specific optimization is not optional — it is the foundation of any serious GEO strategy.

## How to Use This Skill

1. Collect the target URL and the site's primary topic/industry
2. Run each platform checklist below against the site
3. Score each platform on the 0-100 rubric
4. Generate GEO-PLATFORM-OPTIMIZATION.md with per-platform scores, gaps, and action items

---

## Platform 1: Google AI Overviews (AIO)

### How AIO Selects Sources
- 92% of AIO citations come from pages already ranking in the **top 10 organic results** — traditional SEO is the gateway
- However, 47% of citations come from pages ranking **below position 5** — AIO has its own selection logic favoring clarity and directness over raw rank
- AIO strongly favors pages with **clean structure, direct answers, and scannable formatting**
- Featured snippet optimization has ~70% overlap with AIO optimization
- AIO prefers **concise, factual, unambiguous answers** — hedging and filler reduce citation probability

### Optimization Checklist

1. **Question-Based Headings**: Use H2/H3 headings phrased as questions matching real user queries. Check Google's "People Also Ask" for the target topic and mirror those exact phrasings.
2. **Direct Answer in First Paragraph**: After each question heading, provide a clear 1-2 sentence answer immediately. Then expand with supporting detail. The first sentence should be a standalone citation candidate.
3. **Tables and Structured Comparisons**: AIO heavily cites tables. Convert any comparison, pricing, specification, or feature data into HTML tables. Use clear column headers.
4. **Ordered and Unordered Lists**: Step-by-step processes should use ordered lists. Feature lists should use unordered lists. AIO extracts these directly.
5. **FAQ Sections**: Add a dedicated FAQ section with 5-10 real questions. Use proper H3 headings for each question. While FAQPage schema rich results are restricted to govt/health sites since Aug 2023, the content pattern still helps AIO extraction.
6. **Definitions and Glossary Boxes**: For any industry-specific term, provide a clear definition. Format: "**[Term]** is [concise definition]." AIO frequently cites definitions.
7. **Statistics with Sources**: Include specific numbers with attribution. "According to [Source], [statistic]." AIO prefers citeable, specific claims over vague assertions.
8. **Publication Date**: Include a visible publication date and last-updated date. AIO deprioritizes undated content for time-sensitive queries.
9. **Author Byline**: Display author name with credentials. Link to an author page with bio, credentials, and sameAs links.
10. **Page Depth**: Keep target pages within 3 clicks of homepage. AIO rarely cites deep, orphaned content.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Ranks in top 10 for target queries | 20 | 20 if yes, 10 if top 20, 0 if beyond |
| Question-based headings present | 10 | 2 points per question heading, max 10 |
| Direct answers after headings | 15 | 3 points per direct answer, max 15 |
| Tables present for comparison data | 10 | 10 if tables used appropriately, 5 if partial, 0 if absent |
| Lists for processes/features | 10 | 10 if present, 5 if partial |
| FAQ section with 5+ questions | 10 | 10 if 5+, 5 if 1-4, 0 if none |
| Statistics with citations | 10 | 2 points per cited stat, max 10 |
| Publication/updated date visible | 5 | 5 if both dates, 3 if one, 0 if none |
| Author byline with credentials | 5 | 5 if full byline, 3 if name only, 0 if none |
| Clean URL + heading hierarchy | 5 | 5 if H1>H2>H3 clean, 3 if minor issues, 0 if broken |

---

## Platform 2: ChatGPT Web Search

### How ChatGPT Selects Sources
- Uses **Bing's search index** as its foundation (not Google)
- Top citation sources by domain share: **Wikipedia (47.9%)**, Reddit (11.3%), YouTube, major news outlets
- ChatGPT heavily weights **entity recognition** — if your brand exists as a structured entity (Wikipedia, Wikidata, Crunchbase), it is far more likely to be cited
- Prefers **authoritative, well-established sources** over new or niche sites
- Longer, more comprehensive articles get cited more often than short pieces
- ChatGPT tends to cite **the most canonical source** for a claim rather than the original

### Optimization Checklist

1. **Wikipedia Presence**: Check if the brand/person/product has a Wikipedia article. If not, assess notability criteria. If notable, create a draft. If an article exists, ensure it is accurate and current.
2. **Wikidata Entity**: Verify the entity exists on Wikidata (wikidata.org). If not, create a Wikidata item with key properties: instance of, official website, social media links, founding date, headquarters location.
3. **Bing Webmaster Tools**: Verify the site is registered in Bing Webmaster Tools. Submit sitemap. Check for crawl errors.
4. **Bing Index Coverage**: Use `site:domain.com` on Bing to verify key pages are indexed. Bing may have different indexed pages than Google.
5. **Reddit Authority**: Check for brand mentions on Reddit. Identify relevant subreddits. Assess whether the brand participates authentically in discussions.
6. **YouTube Presence**: Verify YouTube channel exists with relevant content. Video descriptions should contain full URLs and entity information.
7. **Authoritative Backlinks**: ChatGPT/Bing weight .edu, .gov, and major publication backlinks heavily. Audit backlink profile for these sources.
8. **Entity Consistency**: Brand name, founding date, leadership, and key facts must be consistent across Wikipedia, Crunchbase, LinkedIn, and the official website.
9. **Comprehensive Content**: Pages targeting ChatGPT citation should be **2000+ words** with thorough topic coverage. ChatGPT prefers single authoritative sources over combining multiple thin pages.
10. **Clear Attribution**: Include "About" sections, company descriptions, and founding stories. ChatGPT uses these for entity grounding.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Wikipedia article exists and is accurate | 20 | 20 if exists, 10 if stub, 0 if none |
| Wikidata entity with 5+ properties | 10 | 10 if complete, 5 if basic, 0 if none |
| Bing index coverage of key pages | 10 | 10 if full, 5 if partial, 0 if poor |
| Reddit brand mentions (positive) | 10 | 10 if active discussions, 5 if mentions, 0 if none |
| YouTube channel with relevant content | 10 | 10 if active, 5 if present but sparse, 0 if none |
| Authoritative backlinks (.edu, .gov, press) | 15 | 3 points per authoritative backlink category, max 15 |
| Entity consistency across platforms | 10 | 10 if consistent, 5 if minor discrepancies, 0 if major |
| Content comprehensiveness (2000+ words) | 10 | 10 if thorough, 5 if adequate, 0 if thin |
| Bing Webmaster Tools configured | 5 | 5 if verified, 0 if not |

---

## Platform 3: Perplexity AI

### How Perplexity Selects Sources
- Top citation sources: **Reddit (46.7%)**, Wikipedia, YouTube, major publications
- Perplexity places the **heaviest emphasis on community validation** of all AI search platforms
- Strongly favors **discussion threads** where claims are debated, validated, or expanded by multiple participants
- Prefers recent content — publication date is a strong ranking signal
- Cites **multiple sources per answer** (typically 5-15), so there is more opportunity for mid-authority sites to appear
- Uses its own crawling infrastructure in addition to search APIs

### Optimization Checklist

1. **Active Reddit Presence**: The brand or its representatives should participate authentically in relevant subreddit discussions. Not promotional — helpful, specific, and community-oriented.
2. **Reddit AMAs and Threads**: Encourage or participate in AMAs, detailed discussion threads, and community Q&As. Perplexity treats these as high-signal content.
3. **Forum and Community Presence**: Beyond Reddit, check Hacker News, Stack Overflow, Quora, and niche industry forums. Perplexity indexes these heavily.
4. **Discussion-Friendly Content**: Publish content that invites discussion — opinion pieces, research findings, contrarian takes, original data. Content that gets shared and debated in communities ranks higher.
5. **Freshness Signals**: Publish content with clear dates. Update content regularly. Perplexity deprioritizes stale content more aggressively than other platforms.
6. **Multiple Source Validation**: Claims in your content should be supported by other sources. Perplexity cross-references and prefers claims it can verify from multiple origins.
7. **YouTube Video Content**: Create video content that Perplexity can reference. Ensure video titles, descriptions, and transcripts contain target information.
8. **Direct, Quotable Passages**: Write paragraphs that can stand alone as citations. Each paragraph should make one clear point with supporting evidence.
9. **Original Data and Research**: Publish original surveys, benchmarks, case studies, or datasets. Perplexity heavily favors primary sources.
10. **Perplexity Pages**: Check if Perplexity has created a "Page" about your topic/brand. These are curated summaries that influence future citations.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Active Reddit presence in relevant subreddits | 20 | 20 if active contributor, 10 if mentioned, 0 if absent |
| Forum/community mentions (HN, SO, Quora) | 10 | 10 if multiple platforms, 5 if one, 0 if none |
| Content freshness (updated within 6 months) | 10 | 10 if recent, 5 if within year, 0 if older |
| Original research/data published | 15 | 15 if original research, 10 if case studies, 5 if some data, 0 if none |
| YouTube content with transcripts | 10 | 10 if active channel, 5 if some videos, 0 if none |
| Quotable, standalone paragraphs | 10 | 2 points per well-structured quotable paragraph, max 10 |
| Multi-source claim validation | 10 | 10 if claims well-sourced, 5 if some sourcing, 0 if none |
| Discussion-generating content | 10 | 10 if content gets shared/discussed, 5 if some engagement, 0 if none |
| Wikipedia/Wikidata presence | 5 | 5 if present, 0 if absent |

---

## Platform 4: Google Gemini

### How Gemini Selects Sources
- Uses **Google's search index** plus strong weighting toward **Google-owned properties**
- YouTube content is weighted significantly more heavily than in standard Google Search
- Google Business Profile data is directly accessible to Gemini
- Gemini uses Google's Knowledge Graph directly — entity presence in Knowledge Graph is a major advantage
- Structured data (Schema.org) is consumed directly by Gemini for entity understanding
- Gemini multi-modal: can reference images, videos, and text together

### Optimization Checklist

1. **Google Knowledge Panel**: Check if the brand has a Google Knowledge Panel. If not, claim it through Google Business Profile or structured data. Ensure all information is accurate.
2. **Google Business Profile**: Complete and optimize GBP with all fields: hours, services, photos, posts, Q&A. Gemini pulls directly from GBP for local queries.
3. **YouTube Strategy**: Create YouTube content for every key topic. Optimize titles, descriptions, timestamps, and closed captions. Gemini cites YouTube more than any other AI platform.
4. **YouTube Chapters and Timestamps**: Use chapters (timestamps in description) so Gemini can reference specific segments of videos.
5. **Google Merchant Center**: For e-commerce, ensure products are in Google Merchant Center. Gemini references product data directly.
6. **Structured Data (Schema.org)**: Implement comprehensive Schema.org markup. Gemini uses this for entity understanding more aggressively than other platforms.
7. **Google Sites Ecosystem**: Ensure presence across Google ecosystem: Google Scholar (for research), Google News (for publishers), Google Maps (for local).
8. **Image Optimization**: Gemini is multi-modal. Use descriptive alt text, structured image filenames, and high-quality images. Include relevant images with every piece of content.
9. **Google E-E-A-T Signals**: All standard Google E-E-A-T signals apply with extra weight. Author pages, about pages, editorial policies, and expertise demonstrations.
10. **Chrome Web Store / Google Workspace Marketplace**: For software companies, presence on Google platforms adds entity signals.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Google Knowledge Panel exists | 15 | 15 if complete, 10 if partial, 0 if none |
| Google Business Profile complete | 10 | 10 if fully optimized, 5 if basic, 0 if none |
| YouTube channel with topic-relevant content | 20 | 20 if active with chapters, 10 if present, 0 if none |
| Schema.org structured data implemented | 15 | 15 if comprehensive, 10 if basic, 5 if minimal, 0 if none |
| Google ecosystem presence (Scholar, News, Maps) | 10 | 10 if 3+, 5 if 1-2, 0 if none |
| Image optimization (alt text, filenames) | 10 | 10 if all images optimized, 5 if partial, 0 if none |
| E-E-A-T signals (author pages, about, editorial) | 10 | 10 if strong, 5 if partial, 0 if weak |
| Google Merchant Center (if e-commerce) | 5 | 5 if applicable and active, N/A otherwise |
| Multi-modal content (text + images + video) | 5 | 5 if rich multi-modal, 3 if some, 0 if text-only |

---

## Platform 5: Bing Copilot

### How Copilot Selects Sources
- Uses **Bing's search index** (shared infrastructure with ChatGPT but different ranking/selection)
- Supports **IndexNow protocol** for near-instant indexing of new and updated content
- Copilot tends to cite **fewer sources per answer** (typically 3-5) but gives more prominent attribution
- Microsoft ecosystem integration: LinkedIn, GitHub, Microsoft Learn content is weighted
- Copilot prefers pages with clear, structured markup and fast load times

### Optimization Checklist

1. **Bing Webmaster Tools**: Register and verify site. Submit XML sitemap. Review and fix any crawl issues.
2. **IndexNow Implementation**: Implement the IndexNow protocol to notify Bing of content changes in real-time. Submit a key file at `/.well-known/indexnow-key.txt` and ping the IndexNow API on content publish/update.
3. **LinkedIn Company Page**: Ensure the company LinkedIn page is complete with accurate description, employee connections, and regular posts. Copilot indexes LinkedIn content.
4. **GitHub Presence**: For tech companies, maintain an active GitHub presence. Copilot references GitHub repos, documentation, and README files.
5. **Microsoft Learn / Documentation**: If relevant, contribute to Microsoft Learn or ensure documentation is compatible with Microsoft's documentation standards.
6. **Bing Places for Business**: Equivalent to Google Business Profile. Complete all fields for local search visibility in Copilot.
7. **Clear Meta Descriptions**: Bing/Copilot weights meta descriptions more heavily than Google does. Write compelling, keyword-rich meta descriptions for every page.
8. **Social Signals**: Bing has historically weighted social signals (shares, likes, engagement) more than Google. Maintain active social media presence.
9. **Exact-Match Keywords**: Bing's algorithm is more literal about keyword matching than Google. Include exact target phrases in titles, headings, and body content.
10. **Fast Page Load**: Copilot deprioritizes slow pages. Target sub-2-second load time. Optimize images, enable compression, minimize render-blocking resources.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Bing Webmaster Tools verified + sitemap | 15 | 15 if verified, 5 if partial, 0 if not |
| IndexNow protocol implemented | 15 | 15 if active, 0 if not |
| Bing index coverage of key pages | 10 | 10 if full, 5 if partial, 0 if poor |
| LinkedIn company page (complete) | 10 | 10 if complete, 5 if basic, 0 if none |
| GitHub presence (if applicable) | 5 | 5 if active, N/A if not applicable |
| Meta descriptions optimized | 10 | 10 if all key pages, 5 if partial, 0 if missing |
| Social media engagement signals | 10 | 10 if active engagement, 5 if present, 0 if none |
| Exact-match keywords in titles/headings | 10 | 10 if well-optimized, 5 if partial, 0 if not |
| Page load speed < 2 seconds | 10 | 10 if < 2s, 5 if < 4s, 0 if > 4s |
| Bing Places configured (if local) | 5 | 5 if complete, N/A if not local |

---

---

## Platform 6: Claude (Anthropic)

### How Claude Selects Sources
- Claude uses **ClaudeBot** for web crawling and **claude.ai web search** for real-time queries
- Strongly favors sites with a **`llms.txt` file** at the root — this is the highest-signal optimization specifically for Claude
- Prioritizes content that is **structurally clean and self-contained** — passages that answer a question without requiring surrounding context
- Heavy weight on **E-E-A-T signals** : named authors, credentials, first-hand experience
- Prefers **server-side rendered content** (Claude's crawler does limited JS execution)
- Respects `ClaudeBot` directives in `robots.txt` explicitly
- Citation behavior: Claude tends to cite **primary sources** and avoids aggregators

### Optimization Checklist

1. **llms.txt file**: Create and maintain `/llms.txt` at the domain root with structured plain-text description of the site: name, description, key pages with URLs, NAP if local business. This is Claude-specific and high-impact.
2. **ClaudeBot access**: Verify `ClaudeBot` is not blocked in `robots.txt`. Add an explicit `Allow: /` rule for ClaudeBot.
3. **Self-contained answer blocks**: Each paragraph should answer one question completely without requiring context. Target 80-150 words per block. Open with the key claim.
4. **Named authorship**: Add visible author names, bios, and credentials to all content pages. Claude weights named expertise heavily.
5. **Structured headings as questions**: Use H2/H3 headings in question format ("Quels sont les horaires ?", "Comment commander ?") — Claude extracts these as answer targets.
6. **Schema.org markup**: Implement JSON-LD for the primary entity type (Restaurant, Organization, Article, etc.). Claude reads structured data to validate factual claims.
7. **Factual density**: Include specific numbers, dates, addresses, and measurable claims. Claude prefers high-specificity content over general descriptions.
8. **Consistent NAP/entity data**: Name, address, phone, and key facts must match across the page, schema markup, and llms.txt. Inconsistencies reduce citation confidence.
9. **No AI-detection red flags**: Avoid generic padding, repetitive restatement, and hedging overload — Claude is trained to recognize low-quality generated content and deprioritizes it.
10. **HTTPS + accessibility**: Claude's crawler respects security signals. HTTPS, fast load times, and accessible HTML structure improve crawl completeness.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| llms.txt present and well-formed | 25 | 25 if complete, 10 if minimal, 0 if absent |
| ClaudeBot explicitly allowed in robots.txt | 10 | 10 if explicit Allow, 5 if allowed by wildcard, 0 if blocked |
| Self-contained answer blocks (80-150 words) | 15 | 3 pts per qualifying block, max 15 |
| Named author with credentials | 10 | 10 if full bio, 5 if name only, 0 if absent |
| Schema.org JSON-LD for primary entity | 15 | 15 if complete, 8 if partial, 0 if absent |
| Question-format H2/H3 headings | 10 | 2 pts per question heading, max 10 |
| Factual density (numbers, dates, specifics) | 10 | 10 if high, 5 if moderate, 0 if generic |
| HTTPS + SSR (no JS-only content) | 5 | 5 if both, 2 if HTTPS only, 0 if issues |

---

## Platform 7: Mistral (Le Chat / La Plateforme)

### How Mistral Selects Sources
- Mistral Le Chat uses **web search** powered by a mix of indexes (Brave Search API + own crawling)
- Strong bias toward **French and European sources** — highest relevance for .fr domains and French-language content
- Favors **official, primary sources** : documentation officielle, sites gouvernementaux, pages entreprises, annuaires reconnus
- Mistral's crawler (**MistralBot**, encore en déploiement) respecte les robots.txt standards
- Cite préférentiellement les sources avec **contenu structuré et daté** (dates de publication visibles)
- Sensible au **contexte géographique** : pour une requête locale française, privilégie les sources françaises vérifiables (Pages Jaunes, Yelp FR, TripAdvisor FR, Google Maps FR)
- Particulièrement influencé par les **annuaires professionnels français** : Societe.com, Verif.com, Infogreffe, SIRET visible

### Optimization Checklist

1. **Présence sur les annuaires français** : S'inscrire sur Pages Jaunes, Societe.com (fiche SIRET visible), Kompass, Yelp France. Mistral indexe ces sources comme validation d'entité pour les requêtes locales françaises.
2. **SIRET visible sur le site** : Afficher le numéro SIRET/SIREN dans les mentions légales ET dans le schema.org `Organization`. Mistral croise ces données avec les registres officiels.
3. **Contenu en français natif** : Éviter les traductions automatiques. Mistral pénalise les contenus qui semblent traduits. Le français courant et idiomatique est fortement privilégié.
4. **Dates de publication visibles** : Afficher `Publié le` et `Mis à jour le` sur toutes les pages éditoriales. Mistral privilégie la fraîcheur de façon agressive.
5. **Sources officielles citées** : Lier vers des sources françaises reconnues (service-public.fr, legifrance.fr pour le légal, insee.fr pour les données). Mistral poids les sites qui citent des autorités françaises.
6. **Google Business Profile complet** : Mistral's web search intègre les données Google Maps pour les requêtes locales françaises. GBP complet = forte visibilité dans Le Chat pour les requêtes "restaurant japonais Trets".
7. **Contenu question/réponse en français** : Structurer des sections FAQ en français naturel avec les formulations exactes des requêtes utilisateurs ("Où se trouve...", "Est-ce que... livre à domicile ?", "Quels sont les horaires de...").
8. **Schema.org en français** : Les valeurs textuelles dans les schémas JSON-LD (description, servesCuisine, addressRegion) doivent être en français. Mistral les lit et les utilise pour les réponses.
9. **TripAdvisor et TheFork FR** : Ces deux plateformes sont fortement indexées par Mistral pour les requêtes restauration en France. Une fiche complète avec avis est un signal de validation critique.
10. **robots.txt ouvert** : S'assurer qu'aucun wildcard ne bloque MistralBot. Ajouter une règle explicite `User-agent: MistralBot` + `Allow: /` dès que le crawler sera en production.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Annuaires français (Pages Jaunes, Societe.com, Kompass) | 20 | 7 pts par annuaire confirmé, max 20 |
| SIRET visible site + schema.org | 10 | 10 si les deux, 5 si l'un des deux, 0 si absent |
| Google Business Profile complet (photos, horaires, avis) | 20 | 20 si complet, 10 si basique, 0 si absent |
| TripAdvisor / TheFork présence FR | 15 | 15 si les deux, 8 si l'un, 0 si absent |
| Dates publication visibles sur pages éditoriales | 10 | 10 si systématiques, 5 si partielles, 0 si absentes |
| Contenu FAQ en français natif | 10 | 2 pts par Q/R bien formée, max 10 |
| Schema.org valeurs en français | 5 | 5 si complet, 2 si partiel, 0 si absent |
| MistralBot non bloqué en robots.txt | 10 | 10 si Allow explicite, 5 si wildcard permissif, 0 si bloqué |

--

## Cross-Platform Summary

### Universal Optimization Actions (help ALL platforms)
1. Wikipedia/Wikidata entity presence
2. YouTube channel with relevant content
3. Comprehensive, well-structured content with clear headings
4. Schema.org structured data (especially Organization + sameAs)
5. Fast page load and clean HTML
6. Author pages with credentials and sameAs links
7. Regular content updates with visible dates

### Platform-Specific Priorities
| Priority | Google AIO | ChatGPT | Perplexity | Gemini | Copilot |
|---|---|---|---|---|---|
| #1 | Top-10 ranking | Wikipedia | Reddit presence | YouTube | IndexNow |
| #2 | Q&A structure | Entity graph | Original research | Knowledge Panel | Bing WMT |
| #3 | Tables/lists | Bing SEO | Freshness | Schema.org | LinkedIn |
| #4 | Featured snippets | Reddit | Community forums | GBP | Meta descriptions |

---

## Output Format

Generate **GEO-PLATFORM-OPTIMIZATION.md** with the following structure:

```markdown
# GEO Platform Optimization Report — [Domain]
Date: [Date]

## Overall Platform Readiness
- Combined GEO Score: XX/100 (average of all platform scores)

## Platform Scores
| Platform | Score | Status |
|---|---|---|
| Google AI Overviews | XX/100 | [Strong/Moderate/Weak] |
| ChatGPT Web Search | XX/100 | [Strong/Moderate/Weak] |
| Perplexity AI | XX/100 | [Strong/Moderate/Weak] |
| Google Gemini | XX/100 | [Strong/Moderate/Weak] |
| Bing Copilot | XX/100 | [Strong/Moderate/Weak] |

Status thresholds: Strong = 70+, Moderate = 40-69, Weak = 0-39

## Platform Details
[Per-platform breakdown with score, gaps found, specific actions]

## Prioritized Action Plan
### Quick Wins (this week)
[Actions that improve multiple platform scores with minimal effort]

### Medium-Term (this month)
[Actions requiring content creation or technical changes]

### Strategic (this quarter)
[Actions requiring entity building, community development, or platform presence]
```
