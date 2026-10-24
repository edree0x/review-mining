#!/usr/bin/env python3
"""
Script to export competitor review analysis results to Excel format.
Uses pandas and openpyxl under the hood.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any
import pandas as pd

def build_review_dataframe(reviews: List[Dict]) -> pd.DataFrame:
    """Convert review data to DataFrame with proper column structure."""
    rows = []
    
    for review in reviews:
        row = {
            "review_id": review.get("review_id", ""),
            "competitor": review.get("competitor", ""),
            "source": review.get("source", ""),
            "source_url": review.get("source_url", ""),
            "date": review.get("date", ""),
            "rating": review.get("rating", ""),
            "review_text": review.get("review_text", ""),
            "sentiment": review.get("sentiment", "neutral"),
            "theme": review.get("theme", ""),
            "sub_theme": review.get("sub_theme", ""),
            "pain_point": review.get("pain_point", ""),
            "strength": review.get("strength", ""),
            "feature_request": review.get("feature_request", ""),
            "switching_reason": review.get("switching_reason", ""),
            "customer_segment": review.get("customer_segment", ""),
            "verbatim_quote": review.get("verbatim_quote", ""),
            "evidence_quality": review.get("evidence_quality", "Low"),
            "collection_timestamp": review.get("collected_at", ""),
        }
        rows.append(row)
    
    return pd.DataFrame(rows)

def build_themes_dataframe(themes: List[Dict]) -> pd.DataFrame:
    """Convert theme data to DataFrame."""
    data = []
    for theme in themes:
        data.append({
            "theme": theme.get("theme", ""),
            "frequency": theme.get("frequency", 0),
            "severity_score": theme.get("severity_score", 0.0),
            "competitors_affected": theme.get("competitors_affected", ""),
            "representative_quotes": ";|;".join(theme.get("representative_quotes", [])),
            "evidence_count": theme.get("evidence_count", 0)
        })
    return pd.DataFrame(data)

def build_opportunities_dataframe(opportunities: List[Dict]) -> pd.DataFrame:
    """Convert opportunity data to DataFrame."""
    data = []
    for opp in opportunities:
        data.append({
            "opportunity": opp.get("opportunity", ""),
            "priority": opp.get("priority", "Medium"),
            "evidence_count": opp.get("evidence_count", 0),
            "validation_method": opp.get("validation_method", ""),
            "suggested_test": opp.get("suggested_test", ""),
            "theme_source": opp.get("theme_source", ""),
        })
    return pd.DataFrame(data)

def export_to_excel(output_data: Dict[str, Any], output_dir: str = "evals/output"):
    """Export all analysis results to Excel with multiple sheets."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Build dataframes
    reviews_df = build_review_dataframe(output_data.get("reviews", []))
    themes_df = build_themes_dataframe(output_data.get("ranked_themes", []))
    opportunities_df = build_opportunities_dataframe(output_data.get("opportunities", []))
    
    # Create Excel writer
    output_path = os.path.join(output_dir, "competitor_reviews_analysis.xlsx")
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        if not reviews_df.empty:
            reviews_df.to_excel(writer, sheet_name="Raw Reviews", index=False)
        if not themes_df.empty:
            themes_df.to_excel(writer, sheet_name="Pain Theme Ranking", index=False)
        if not opportunities_df.empty:
            opportunities_df.to_excel(writer, sheet_name="Strategic Opportunities", index=False)
        
        # Add metadata sheet
        metadata = pd.DataFrame({
            "Metric": ["Collection Timestamp", "Total Reviews Analyzed", "Successful Sources", "Failed Sources"],
            "Value": [
                output_data.get("timestamp", "N/A"),
                output_data.get("total_reviews_collected", 0),
                output_data.get("successful_sources", 0),
                "; ".join([f"{s}{e}" for s, e in output_data.get("failed_sources", [])])
            ]
        })
        metadata.to_excel(writer, sheet_name="Metadata", index=False)
    
    save_path = os.path.normpath(output_path)
    print(f"Exported analysis to Excel: {save_path}")
    return save_path

# Example usage
if __name__ == "__main__":
    # Mock data for testing
    mock_reviews = [
        {
            "review_id": "R001",
            "competitor": "Competitor A",
            "source": "G2",
            "source_url": "https://www.g2.com/products/competitor-a/reviews",
            "date": "2023-11-15",
            "rating": 2,
            "review_text": "The onboarding process is confusing and takes too long. I had to call support multiple times to get started.",
            "theme": "Onboarding Complexity",
            "sentiment": "negative",
            "evidence_quality": "High"
        },
        {
            "review_id": "R002", 
            "competitor": "Competitor A",
            "source": "Reddit",
            "source_url": "https://www.reddit.com/r/Software/comments/xyz/",
            "date": "2023-12-01",
            "rating": 1,
            "review_text": "Switched to Competitor B after 3 months because their support was faster. Competitor B just cares about customers.",
            "theme": "Customer Support",
            "sentiment": "negative",
            "evidence_quality": "Medium"
        }
    ]
    
    mock_opportunities = [
        {
            "opportunity": "Offer tiered pricing with clearer value communication",
            "priority": "High",
            "evidence_count": 3,
            "validation_method": "Customer interviews + review volume",
            "theme_source": "Pricing Concerns"
        }
    ]
    
    mock_analysis = {
        "reviews": mock_reviews,
        "ranked_themes": [],
        "opportunities": mock_opportunities,
        "timestamp": datetime.now().isoformat()
    }
    
    export_to_excel(mock_analysis)
