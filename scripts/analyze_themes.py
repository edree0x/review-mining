#!/usr/bin/env python3
"""
Script to analyze raw review data and extract themes, patterns, and opportunities.
"""

import json
import os
import re
from collections import defaultdict, Counter
from pathlib import Path
from typing import List, Dict, Any

def load_reviews(data_dir: str = "evals/data") -> List[Dict]:
    """Load all review JSON files from the data directory."""
    reviews = []
    data_dir = Path(data_dir)
    
    if not data_dir.exists():
        print(f"Data directory {data_dir} not found")
        return []
    
    for json_file in data_dir.glob("reviews_*.json"):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                data["source_file"] = str(json_file)
                reviews.extend(data)
        except Exception as e:
            print(f"Error loading {json_file}: {e}")
    
    return reviews

def categorize_problems(reviews: List[Dict]) -> Dict[str, List[Dict]]:
    """Categorize reviews into thematic buckets."""
    categories = defaultdict(list)
    problem_keywords = {
        "pricing": ["price", "cost", "fee", "expensive", "billing", "subscription"],
        "usability": ["confusing", "hard to use", "difficult", "intuitive", "clunky"],
        "performance": ["crash", "slow", "bug", "error", "freeze", "lag"],
        "support": ["support", "service", "help", "response", "slow", "unhelpful"],
        "features": ["missing", "wish", "need", "should", "could", "better"],
        "data_privacy": ["privacy", "security", "access", "data", "leak"],
    }
    
    for review in reviews:
        text = review["review_text"].lower()
        
        for category, keywords in problem_keywords.items():
            if any(keyword.lower() in text for keyword in keywords):
                categories[category].append(review)
                break
    
    return dict(categories)

def extract_verbatim_quotes(reviews: List[Dict], min_occurrences: int = 2) -> Dict[str, List[str]]:
    """Extract significant verbatim quotes from reviews."""
    quote_counter = Counter()
    dropbox = defaultdict(list)
    
    for review in reviews:
        # Extract memorable phrases (short, impactful sentences)
        sentences = re.split(r'(?<=[.!?])\s+', review["review_text"])
        
        for sent in sentences:
            sent_lower = sent.lower().strip()
            # Filter out very short fragments
            if len(sent_lower) > 10:
                # Check if this sentence contains any problem keywords
                for category, keywords in {
                    "pricing": ["price", "cost", "fee", "expensive", "billing", "subscription"],
                    "usability": ["confusing", "hard to use", "difficult", "intuitive", "clunky"],
                    "performance": ["crash", "slow", "bug", "error", "freeze", "lag"],
                    "support": ["support", "service", "help", "response", "slow", "unhelpful"],
                    "features": ["missing", "wish", "need", "need", "better"],
                }.items():
                    if any(kw.lower() in sent_lower for kw in keywords):
                        if len(sent_lower.split()) < 20:  # Keep concise impactful phrases
                            clean_sent = re.sub(r'[^\w\s\'\-!?]', '', sent_lower)
                            if clean_sent and len(clean_sent.split()) > 3:
                                if clean_sent not in dropbox:
                                    dropbox[clean_sent] = {
                                        "review_id": review.get("review_id", ""),
                                        "source_url": review.get("source_url", ""),
                                        "reviewer": review.get("reviewer", ""),
                                        "rating": review.get("rating", ""),
                                        "verbatim": sent_lower
                                    }
    
    # Filter to only those appearing min_occurrences times
    frequent_quotes = {
        quote: details for quote, details in dropbox.items()
        if sum(1 for r in reviews 
               if any(kw in r["review_text"].lower() for kw in list(dropbox.keys()))) >= min_occurrences
    }
    
    return frequent_quotes

def theme_ranking(categories: Dict[str, List[Dict]]) -> List[Dict]:
    """Create ranked list of themes by frequency and severity."""
    theme_ranking = []
    
    for theme, reviews in categories.items():
        count = len(reviews)
        # Simple severity scoring based on negative modifiers
        severity_score = 0
        for review in reviews:
            text = review["review_text"].lower()
            severity_score += len(re.findall(r'frustrated|disappointed|annoyed|outraged|angry|worst|terrible|crash|broken|worst', text))
        
        severity_score = min(severity_score / max(1, count), 5) * count
        
        theme_ranking.append({
            "theme": theme,
            "frequency": count,
            "reviews": count,
            "severity_score": severity_score,
            "representative_quotes": [r["review_text"] for r in reviews[:3]]
        })
    
    # Sort by frequency * severity_score
    theme_ranking.sort(key=lambda x: x["frequency"] * x["severity_score"], reverse=True)
    return theme_ranking

def extract_opportunities(ranked_themes: List[Dict]) -> List[Dict]:
    """Convert ranked themes into actionable business opportunities."""
    opportunities = []
    
    for theme_data in ranked_themes[:5]:  # Top 5 themes
        theme = theme_data["theme"]
        freq = theme_data["frequency"]
        severity = theme_data["severity_score"]
        
        # Determine if this represents a true opportunity
        is_opportunity = freq >= 3 and severity >= 3  # Thresholds
        
        if is_opportunity:
            # Mock opportunity generation based on theme
            opportunity_descriptions = {
                "pricing": "Offer tiered pricing with clearer value communication",
                "usability": "Create interactive onboarding guided tour",
                "performance": "Launch performance monitoring dashboard",
                "support": "Implement 24/7 chat support with guaranteed response times",
                "features": "Develop feature request priority system",
                "data_privacy": "Implement privacy-by-design framework with third-party audit"
            }
            
            opportunity_desc = opportunity_descriptions.get(theme, "Custom solution for unnamed pain point")
            
            opportunities.append({
                "opportunity": opportunity_desc,
                "priority": "High" if severity >= 4 else "Medium",
                "evidence_count": freq,
                "theme_source": theme,
                "examples": theme_data["representative_quotes"]
            })
    
    return opportunities

def generate_analysis_output(reviews: List[Dict], output_dir: str = "evals/output"):
    """Generate all analysis outputs."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Step 1: Categorize
    categories = categorize_problems(reviews)
    
    # Step 2: Rank themes
    ranked_themes = theme_ranking(categories)
    
    # Step 3: Extract opportunities
    opportunities = extract_opportunities(ranked_themes)
    
    # Step 4: Save outputs
    # Raw categorized data
    categories_path = f"{output_dir}/categorized_themes.json"
    with open(categories_path, "w") as f:
        json.dump(dict(categories), f, indent=2)
    
    # Ranked themes
    ranked_path = f"{output_dir}/ranked_themes.json"
    with open(ranked_path, "w") as f:
        json.dump(ranked_themes, f, indent=2)
    
    # Opportunities
    opp_path = f"{output_dir}/opportunities.json"
    with open(opp_path, "w") as f:
        json.dump(opportunities, f, indent=2)
    
    print(f"Analysis outputs saved to {output_dir}")
    return opportunities

# Example usage
if __name__ == "__main__":
    reviews = load_reviews()
    if reviews:
        opportunities = generate_analysis_output(reviews)
        print(f"Found {len(opportunities)} key opportunities:")
        for opp in opportunities:
            print(f"  - {opp['opportunity']} (Priority: {opp['priority']})")
    else:
        print("No reviews found to analyze")
