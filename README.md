# Review Mining Skill

Systematic competitor review mining for extracting customer pain points from multiple review platforms and generating structured Excel analysis.

---

## Install This Skill

Copy and paste this command into your terminal to install the skill:

```bash
npx skills add edree0x/review-mining
```

After installation, the skill will be available in your agent's skill library and can be triggered automatically when you ask about competitor reviews.

---

## What This Skill Does

This skill systematically researches what customers are saying about your competitors' products. It mines reviews from multiple public platforms (G2, Amazon, Reddit, Trustpilot, etc.), extracts authentic customer language, identifies recurring pain points and feature gaps, and converts everything into structured data ready for Excel analysis.

**Think of it as:** A research assistant that reads thousands of competitor reviews for you and tells you exactly what customers love, hate, and wish existed.

---

## How It Works

### Step 1: Identify Competitors
The skill discovers your direct and adjacent competitors based on your product category. It targets 3-5 primary competitors plus 2-3 adjacent alternatives.

### Step 2: Select Review Platforms
Based on your product type, it picks the right review sources:

| Product Type | Primary Sources |
|--------------|----------------|
| SaaS / B2B | G2, Capterra, TrustRadius |
| Physical Products | Amazon, Google Reviews, Trustpilot |
| Developer Tools | GitHub Issues, Reddit, Hacker News |
| Mobile Apps | App Store, Google Play, Product Hunt |
| Services | Trustpilot, Google Reviews, Yelp |

### Step 3: Collect Reviews
The skill collects 15-20 reviews per competitor from each platform, focusing on:
- 1-3 star reviews (pain points and dealbreakers)
- 4-5 star reviews (what users love)
- Recent reviews (last 6-12 months)
- Verified purchases where available

### Step 4: Extract Patterns
It categorizes feedback into themes like:
- **Pricing concerns** (hidden fees, value perception)
- **Usability issues** (confusing onboarding, workflow friction)
- **Performance problems** (bugs, crashes, slow response)
- **Support quality** (response time, resolution effectiveness)
- **Feature gaps** (missing functionality, requested features)

### Step 5: Score and Prioritize
Each theme is scored by:
- **Frequency** (how many reviews mention it)
- **Severity** (how much it hurts users)
- **Business impact** (does it block purchase or usage)

### Step 6: Generate Structured Output
The skill produces an Excel workbook with 5 sheets:
1. **Raw Reviews** - Every review with metadata
2. **Pain Theme Ranking** - Themes ranked by frequency × severity
3. **Competitor Scorecard** - Comparison across competitors
4. **Strategic Opportunities** - Actionable product recommendations
5. **Source Audit** - Data quality and coverage tracking

---

## Output Format

The skill generates structured data including:

- **Raw review exports** (JSON) - All collected reviews with verbatim text
- **Thematic analysis** (JSON) - Categorized pain points with frequency scores
- **Opportunity mapping** (JSON) - Actionable product recommendations
- **Excel workbook** (XLSX) - 5 sheets ready for analysis and sharing

---

## Usage Examples

### Example 1: Analyze a Competitor's Weaknesses
```
"Find the top 3 pain points users complain about with Competitor X on G2 and Reddit"
```

### Example 2: Identify Feature Gaps
```
"What features do users request from Competitor Y that they can't get?"
```

### Example 3: Understand Switching Behavior
```
"Why are users switching from Competitor Z to alternatives?"
```

### Example 4: Full Competitive Audit
```
"Analyze reviews for Competitors A, B, and C across G2, Amazon, and Reddit"
```

---

## Core Components

### Reference Files
- `references/source-matrix.md` - Source selection guide by product category
- `references/analysis-framework.md` - Technical framework for pattern extraction
- `references/schemas.md` - JSON schemas for data structures

### Scripts
- `scripts/collect_reviews.py` - Systematic review collection from multiple sources
- `scripts/analyze_themes.py` - Pattern extraction and opportunity identification
- `scripts/export_xlsx.py` - Excel output generation with structured reporting

### Test Cases
- `evals/evals.json` - Standardized evaluation test cases

---

## Usage Triggers

Activate when user requests:
- "What are users saying about [competitor]?"
- "Find pain points in [product category]"
- "Voice of customer mining"
- "Competitor review analysis"
- "Systematically analyze competitor reviews"
- "Extract patterns from competitor reviews"
- "Create competitor review matrix"
- "Generate insights from competitor reviews"

---

## Implementation Status

✅ Skill structure created
✅ Reference documentation drafted
✅ Test framework established
✅ Automation scripts ready
✅ Excel export capability ready

Ready for skill packaging and evaluation.