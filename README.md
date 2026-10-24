# Competitor Review Mining Skill

This skill provides a systematic approach to research competitor customer pain points by mining reviews across multiple public sources, analyzing patterns, and converting insights into actionable product opportunities.

## Purpose

Extract authentic customer voices from competitor reviews to:
- Identify unmet user needs and pain points
- Discover feature gaps and desired functionality  
- Find switching triggers and decision drivers
- Generate verbatim language for positioning and messaging
- Create structured opportunity pipeline for product strategy

## Core Components

### Reference Files
- `references/source-matrix.md` - Source matrix by product category
- `references/analysis-framework.md` - Technical framework for pattern extraction
- `references/schemas.md` - JSON schemas for data structures

### Scripts
- `scripts/collect_reviews.py` - Systematic review collection from multiple sources
- `scripts/analyze_themes.py` - Pattern extraction and opportunity identification  
- `scripts/export_xlsx.py` - Excel output generation with structured reporting

### Test Cases
- `evals/evals.json` - Standardized evaluation test cases

## Usage Triggers

Activate when user requests:
- "What are users saying about [competitor]?"
- "Find pain points in [product category]"
- "Voice of customer mining" 
- "Competitor review analysis"
- "Systematically analyze competitor reviews"

## Output Format

Generates structured data including:
- Raw review exports (JSON)
- Thematic analysis (JSON)
- Opportunity mapping (JSON) 
- Excel workbook (XLSX) with:
  - Raw Reviews sheet
  - Pain Theme Ranking sheet  
  - Strategic Opportunities sheet
  - Metadata audit trail

## Implementation Status

✅ Skill structure created
✅ Reference documentation drafted  
✅ Test framework established
✅ Automation scripts ready

Ready for skill packaging and evaluation.
