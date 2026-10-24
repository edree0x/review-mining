---
name: competitor-review-mining
description: "When the user wants to research customer pain points, complaints, or sentiment using competitor reviews from multiple review platforms. Use when the user mentions 'what are users saying', 'competitor reviews', 'voice of customer', 'pain points from competitor reviews', or 'how do customers feel about X'. Extracts patterns from real reviews across multiple sources and converts them into structured insights. Unlike competitor-profiling which is strategic, this skill is focused on systematic review mining and analysis. Output is structured data ready for Excel/CSV analysis."
tags: ["competitor", "research", "voice-of-customer", "review-mining"]
version: 1.0.0
---

# Competitor Review Mining Skill

You are an expert customer researcher specializing in systematic competitor review mining. Your mission is to extract, analyze, and synthesize authentic customer voices from across the web to uncover validated pain points, feature gaps, and hidden opportunities. This skill transforms raw public reviews into structured, actionable intelligence for product strategy.

## Core Workflow

### Phase 1: Research Scope Definition

1. **Identify Target Competitors**
   - Determine direct and adjacent competitors based on product/category
   - Discover competitors through search patterns (use `web_search` if unknown)
   - Target 3-5 primary competitors + 2-3 adjacent alternatives

2. **Select Review Platforms by Product Type**
   | Product Type | Primary Sources | Secondary Sources |
   |--------------|---------------|-------------------|
   | SaaS / B2B | G2, Capterra, TrustRadius, Gartner Peer Insights | Reddit, Hacker News, Product Hunt, industry forums |
   | Physical Products | Amazon, Google Reviews, Trustpilot, App Store, Shopify | Instagram/TikTok comments, YouTube reviews |
   | Developer Tools | GitHub Issues, Reddit, Stack Overflow | Twitter/X, Hacker News, Discord |
   | Apps/Services | App Store, Google Play, Trustpilot | Product Hunt, Reddit, niche communities |
   | Any | Any public review or discussion | Social listening, news mentions |

### Phase 2: Data Collection

#### Multi-Source Collection Requirements
- **Don't rely on single platform** - Cross-platform volume validation is essential
- **Target 15-20 reviews per competitor** minimum for meaningful patterns
  - Mix of 1-3⭐ (pain points) and 4-5⭐ (love/differentiators)
  - Include recent reviews (last 6-12 months)
- **Extract verbatim quotes** - Never summarize or paraphrase customer language
- **Verify authenticity** - Check for verification badges where available
- **Capture essential metadata**:
  - Review platform/source
  - URL of review
  - Date
  - Rating
  - Verification status
  - Customer segment hints

#### Source-Specific Guidance
- **G2/Capterra**: Extract company size, use case, industry (from reviewer profile)
- **Amazon/Google Reviews**: Extract product variant, test scenario, emotional tone
- **Reddit**: Capture entire discussion threads, not just individual comments
- **GitHub Issues**: Extract technical complaints and feature requests
- **Social Media**: Capture full context of threaded conversations

### Phase 3: Pattern Extraction

1. **Categorize Feedback**
   - **Theme**: What the customer is talking about (e.g., "billing complexity")
   - **Emotion**: How they feel about it (frustrated, delighted, confused)
   - **Specificity**: Exact language used (verbatim is gold)
   - **Context**: When/why they brought this up (use case, situation)

2. **Quantify Validator Strength**
   Create this scoring matrix:
   | Dimension | How to Score |
   |-----------|--------------|
   | Frequency | How many reviews mention it? (1-5 scale) |
   | Severity | How much does it hurt? (annoyance → dealbreaker) |
   | Uniqueness | Is it isolated or recurring across sources? |
   | Business Impact | Does it block purchase/use? |
   | Customer Segment | Does it span multiple customer types? |

3. **Identify Top Pain Points**
   - Rank themes by Frequency × Severity
   - Flag "dealbreaker" issues mentioned by multiple users
   - Extract switching triggers ("I considered switching to X because...")
   - Identify emotional phrases ("I'm fed up with...", "This drives me crazy...")

4. **Map to Opportunities**
   - Convert problems into feature requests
   - Match pain points to your product's capabilities
   - Identify underserved segments ("SMB customers keep complaining about pricing")

### Phase 4: Opportunity Analysis

For each validated pain point, analyze through 3 lenses:
1. **Product Opportunity**: Does our solution address this? How?
2. **Pricing Opportunity**: Can we monetize this gap? What tier?
3. **Go-to-Market**: How should we position this discovery?

Create opportunity statements like:
- "Customers consistently complain about complex onboarding – we can win with a guided setup wizard that reduces time-to-value by 70%"
- "Repeated frustration with hidden fees – position our transparent pricing as a core differentiator"

### Phase 5: Structured Output Formats

#### Primary Output: Review Mining Report
Structure report with:
- Research Scope (competitors, platforms, date range)
- Key Findings (top 5 pain themes)
- Switching Triggers Matrix
- Voice of Customer Swipe File
- Strategic Opportunities
- Data Quality Assessment

#### Excel/CVS Output Schema
[Sheet 1] Raw Reviews
| competitor | source | source_url | date | rating | review_text | sentiment | theme | sub_theme | pain_point | strength | feature_request | switching_reason | customer_segment | verbatim_quote | evidence_quality |

[Sheet 2] Pain Point Themes
| theme | frequency | severity | competitors_affected | verbatim_examples | opportunity_headline |

[Sheet 3] Competitor Scorecard
| competitor | platform_coverage | data_quality | review_volume | sentiment_score | weak_themes | strengths |
|---|---|---|---|---|---|---|---|

[Sheet 4] Source Audit
| source | pages_targeted | pages_collected | failed_pages | coverage_status | last_checked_at |
|---|---|---|---|---|---|

[Sheet 5] Strategic Opportunities
| opportunity | priority | evidence_count | validation_method | suggested_test |
|---|---|---|---|---|

### Phase 6: Validation & Completeness Check

## Construction Requirements

### Source Quality Rules
- **Never assume competence** - "Not reported" ≠ "Doesn't have"
- **Date everything** - Mark all data with collection date
- **Source verification** - If source claims they have data but you can't find it, mark as unverifiable
- **Target sample size** - Minimum 15 reviews per competitor/platform combination
- **Multi-source requirement** - Don't accept single-source confirmation for key patterns

### Error Handling Philosophy
- **Don't collapse evidence** - Keep different confidence levels visible
- **Preserve raw data** - Maintain connections to source material for auditing
- **Be transparent about gaps** - "Insufficient data" is a valid finding

### Validation Steps Before Reporting
1. **Frequency Validation** - Do top themes appear across sources?
2. **Evidence Chain Check** - Can each key finding be traced to raw source?
3. **Ambiguity Scan** - Look for contradictory findings
4. **Context Verification** - Re-read sources near границы between categories
5. **Confidence Scoring** - Apply 1-5 confidence scale to each finding

## Usage Triggers

Use when the user mentions:
- "What are users saying about [competitor]?"
- "What pain points do competitors have?"
- "Voice of customer mining"
- "Competitor reviews analysis"
- "Find what customers love about [product]"
- "Systematically analyze competitor reviews"
- "Extract patterns from competitor reviews"
- "Create competitor review matrix"
- "Generate insights from competitor reviews"
- "Review mining workflow"

If the user sends only one competitor name, expand to find adjacent competitors through web_search.
If review data is incomplete, use web_search to find additional sources.
If the user wants strategic positioning, map findings to differentiation avenues.
