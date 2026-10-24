# Source Matrix for Competitor Review Mining

This document defines the systematic approach to identifying, accessing, and analyzing reviews across different product categories.

## Source Selection by Product Category

Different product types require different review sources for authentic, high-signal feedback.

### B2B SaaS & Software
| Source | Access Method | Key Strengths | Limitations |
|--------|-------------|---------------|-------------|
| G2 | Direct access via G2 MCP | Verified user profiles, company metadata | Limited to software categories, can be slow |
| Capterra | Direct access via Capterra MCP | Broad category coverage | Similar limitations to G2, fewer verification controls |
| TrustRadius | Direct access via TRP | High user verification rate | Smaller sample size, less frequent updates |
| Gartner Peer Insights | Direct access via Gartner MCP | Enterprise-grade insights | Expensive, enterprise-focused scope |
| LinkedIn | File search on `site:linkedin.com/in "[job title] competitor"` | Targeted professional audience | Low volume, high signal |

### B2C / Consumer Products
| Source | Access Method | Key Strengths | Limitations |
|--------|-------------|---------------|-------------|
| Amazon | File search on `site:amazon.com "[product]" reviews` | Massive volume, verified purchases | Review gating, fake reviews possible |
| Google Reviews | Direct access via Google Maps API | Broad geographic coverage | Business-specific, can be gamed |
| Trustpilot | Direct access via Trustpilot MCP | Enterprise verification program | Smaller sample than Amazon |
| Instagram/TikTok | Keyword search in comments | Authentic consumer language | Hard to scale, hard to filter sentiment |
| Instagram/TikTok | Keyword search in comments | Authentic consumer language | Hard to scale, hard to filter sentiment |

### Developer Tools & Technical Products
| Source | Access Method | Key Strengths | Limitations |
|--------|-------------|---------------|-------------|
| GitHub Issues | `site:github.com "[tool]" issues` or GitHub API | Technical complaints, feature requests | Skews technical users, may miss broader audience |
| Reddit | `site:reddit.com "[tool]" r/[relevant_subreddit]` | Honest, unfiltered feedback | Community bias toward vocal minority |
| Hacker News | `site:news.ycombinator.com "[tool]"` | Technical depth, skeptical audience | Small sample, opinion-heavy |
| Product Hunt | `prodhunt.com/search?q=[tool]` | Emerging tools, early adopter signals | Early-stage bias, hype-driven |

### Physical Products & Services
| Source | Access Method | Key Strengths | Limitations |
|--------|-------------|---------------|-------------|
| Amazon | File search on `site:amazon.com "[product]" reviews` | Massive volume, photo reviews | Review gating, incentivized reviews |
| Google Reviews | Direct access via Maps API | Local search coverage | Business-specific, can be gamed |
| Yelp | `site:yelp.com "[business]" reviews` | Experience-focused, local | Smaller sample than Amazon |
| Platform-specific | Apple App Store, Google Play | Mobile-specific feedback | App-store specific issues only |

### Community & Social Spaces
| Source | Access Method | Strengths | Limitations |
|--------|-------------|-----------|-------------|
| Reddit | `site:reddit.com "[topic]"` + subcategorization | Deep threads, user verification via upvotes | Subreddit-specific bias |
| X/Twitter | `site:x.com "[product]"` | Real-time reactions, influencer mentions | 280-character limit distorts nuance |
| YouTube Comments | `site:youtube.com "[Video Title]"` | Visual product feedback | Video-driven sentiment only |
| Indie Hackers | `site:indiehackers.com "[problem]"` | Founder-to-founder insights | Small sample, selective audience |

## Source Quality Scoring Matrix

| Source Type | Retrieval Difficulty | Verification Level | Sample Size | Sentiment Precision | Recommended Minimum | Notes |
|-------------|----------------------|--------------------|-------------|-------------------|----------------------|-------|
| Direct API (G2, Capterra, TrustRadius) | Low | High (verified users) | Medium (100s) | High | ≥15 reviews per competitor | Leverage official MCPs when available |
| File Search (Amazon, Google, etc.) | Medium | Medium | High (1000s) | Medium | ≥30 reviews | Use advanced search operators |
| Web Search (Reddit, Forum) | Low | Medium | Medium | Low | ≥10 comments | Use precise operators (`"frustrated with" AND "pricing"`) |
| API-Driven (Twitter) | Medium | Medium | Medium | Medium | ≥20 posts | Use v2 endpoints with rate limiting |

## Building the Source Matrix

Create a dynamic matrix that maps:
- Competitor → Target Product Type → Primary Sources → Secondary Sources → Validation Status

This matrix becomes the foundation for the scraping strategy and ensures systematic coverage across all relevant data sources without relying on any single platform's limitations.

