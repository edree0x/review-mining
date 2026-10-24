#!/usr/bin/env python3
"""
Script to systematically collect competitor reviews from multiple sources.
Designed for multi-platform source coverage with proper error handling.
"""

import json
import time
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Mock functions representing actual scraping logic
# These would be replaced with actual implementation using Playwright/Apify etc.

def search_competitors(query: str, limit: int = 5) -> List[Dict]:
    """Mock competitor discovery function."""
    # In reality, this would use web_search or similar
    mock_results = [
        {"name": "Competitor A", "domain": "competitor-a.com", "type": "B2B SaaS"},
        {"name": "Competitor B", "domain": "competitor-b.com", "type": "B2C App"},
        {"name": "Competitor C", "domain": "competitor-c.com", "type": "Physical Product"},
    ]
    return mock_results[:limit]

def get_review_sources(competitor: str) -> List[Tuple[str, str]]:
    """Mock function to return source URLs for a competitor."""
    mock_sources = {
        "Competitor A": [
            ("https://www.g2.com/products/competitor-a/reviews", "g2"),
            ("https://www.capterra.com/products/competitor-a/reviews", "capterra"),
            ("https://www.trustpilot.com/review/competitor-a.com", "trustpilot")
        ],
        "Competitor B": [
            ("https://www.amazon.com/product-reviews/B09VXJ3Y3D", "amazon"),
            ("https://www.reddit.com/r/appname/comments/1a2b3c/rating/", "reddit"),
            ("https://www.producthunt.com/product/company-name", "producthunt")
        ],
        "Competitor C": [
            ("https://www.youtube.com/watch?v=example", "youtube"),
            ("https://www.trustpilot.com/review/competitor-c.com", "trustpilot"),
            ("https://www.appstore.com/app/competitor-c", "appstore")
        ]
    }
    return mock_sources.get(competitor, [])

def scrape_reviews(source_url: str, source_type: str) -> List[Dict]:
    """Mock review scraper with source-specific logic."""
    print(f"Scraping {source_type} from {source_url}")
    
    # Simulate different scraping approaches by source type
    if source_type == "g2":
        return [{
            "platform": "G2",
            "source_url": source_url,
            "rating": 3,
            "date": "2023-11-15",
            "text": "The onboarding process is confusing and takes too long. I had to call support multiple times to get started.",
            "verified_purchase": True,
            "source": "g2"
        }]
    elif source_type == "amazon":
        return [{
            "platform": "Amazon",
            "source_url": source_url,
            "rating": 2,
            "date": "2023-12-01",
            "text": "Had to return it because it didn't work with my existing system. Very frustrating.",
            "verified_purchase": True,
            "source": "amazon"
        }]
    elif source_type == "reddit":
        return [{
            "platform": "Reddit",
            "source_url": source_url,
            "rating": 1,
            "date": "2024-01-20",
            "text": "Switched to Competitor A after 3 months because their support was faster. Competitor A just cares about customers.",
            "verified_purchase": False,
            "source": "reddit"
        }]
    elif source_type == "trustpilot":
        return [{
            "platform": "Trustpilot",
            "source_url": source_url,
            "rating": 2,
            "date": "2023-10-10",
            "text": "Very poor customer service experience. Waited 3 days for a response that never came.",
            "verified_purchase": True,
            "source": "trustpilot"
        }]
    elif source_type == "youtube":
        return [{
            "platform": "YouTube Comments",
            "source_url": source_url,
            "rating": 1,
            "date": "2024-02-15",
            "text": "Disappointed - the app crashed every time I tried to export my work. Shouldn't happen at this price point.",
            "verified_purchase": False,
            "source": "youtube_comments"
        }]
    else:
        return [{
            "platform": source_type.upper(),
            "source_url": source_url,
            "rating": 3,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "text": f"General sentiment towards {competitor} from this source. Needs deeper extraction.",
            "verified_purchase": False,
            "source": source_type
        }]

def collect_competitor_reviews(competitor_name: str) -> Dict:
    """Main collection function."""
    print(f"=== Collecting reviews for {competitor_name} ===")
    
    # Step 1: Find sources
    sources = get_review_sources(competitor_name)
    if not sources:
        print(f"No sources found for {competitor_name}")
        return {}
    
    all_reviews = []
    failed_sources = []
    
    for source_url, source_type in sources:
        try:
            reviews = scrape_reviews(source_url, source_type, competitor_name)
            all_reviews.extend(reviews)
        except Exception as e:
            print(f"Failed to scrape {source_type} from {source_url}: {e}")
            failed_sources.append((source_type, str(e)))
    
    # Step 2: Validate and enrich
    validated_reviews = []
    for review in all_reviews:
        # Add collection metadata
        review["collected_at"] = datetime.now().isoformat()
        review["competitor"] = competitor_name
        review["collection_status"] = "success" if review["source"] != "failed" else "failed"
        
        # Score evidence quality (1-5)
        evidence_quality = 5 if review.get("verified_purchase") else 3
        review["evidence_quality"] = evidence_quality
        
        validated_reviews.append(review)
    
    return {
        "competitor": competitor_name,
        "reviews": validated_reviews,
        "failed_sources": failed_sources,
        "total_reviews_collected": len(validated_reviews),
        "sources_scraped": len(sources)
    }

def save_collected_data(review_data: Dict, output_dir: str = "evals/data"):
    """Save raw review data to structured files."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    competitor_name = review_data["competitor"]
    clean_name = "".join(c for c in competitor_name if c.isalnum() or c in "-_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save raw reviews
    reviews_path = f"{output_dir}/reviews_{clean_name}_{clean_name}_{timestamp}.json"
    with open(reviews_path, "w") as f:
        json.dump(review_data["reviews"], f, indent=2, ensure_ascii=False)
    
    # Save metadata
    metadata_path = f"{output_dir}/metadata_{clean_name}_{timestamp}.json"
    with open(metadata_path, "w") as f:
        json.dump({
            "competitor": review_data["competitor"],
            "collection_timestamp": review_data.get("collected_at"),
            "total_reviews": review_data["total_reviews"],
            "successful_sources": len([r for r in review_data["reviews"] if r["source"] != "failed"]),
            "failed_sources": review_data["failed_sources"],
            "source_metadata": {
                url: status for url, status in review_data.get("failed_sources", [])
            }
        }, f)
    
    print(f"Saved collected data to {reviews_path}")
    return {"reviews": reviews_path, "metadata": metadata_path}

# Example usage that would normally be triggered by CLI
if __name__ == "__main__":
    competitor = "Competitor A"
    collected = collect_competitor_reviews(competitor)
    saved_paths = save_collected_data(collected)
    print(f"Collection complete. Raw data saved to: {saved_paths}")
