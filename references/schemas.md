# JSON Schemas for Competitor Review Mining

## Review Data Schema

```json
{
  "review_id": "optional identifier",
  "competitor": "string",
  "source": "string", 
  "source_url": "string",
  "date": "YYYY-MM-DD",
  "rating": "integer (1-5)",
  "review_text": "string",
  "sentiment": "string (positive/neutral/negative)",
  "theme": "string",
  "sub_theme": "string",
  "pain_point": "string",
  "strength": "string",
  "feature_request": "string",
  "switching_reason": "string",
  "customer_segment": "string",
  "verbatim_quote": "string",
  "evidence_quality": "string (High/Medium/Low)",
  "collection_timestamp": "ISO timestamp"
}
```

## Theme Schema

```json
{
  "theme": "string",
  "frequency": "integer",
  "severity_score": "float (0-5)",
  "competitors_affected": "string or array",
  "representative_quotes": [
    {
      "quote": "string",
      "source_url": "string"
    }
  ],
  "evidence_count": "integer"
}
```

## Opportunity Schema

```json
{
  "opportunity": "string",
  "priority": "string (High/Medium/Low)",
  "evidence_count": "integer",
  "validation_method": "string",
  "suggested_test": "string",
  "theme_source": "string"
}
```

## Output Data Structure

```json
{
  "timestamp": "ISO timestamp",
  "total_reviews_collected": "integer",
  "successful_sources": "integer",
  "failed_sources": [
    {
      "source_type": "string",
      "error_message": "string"
    }
  ],
  "reviews": [Review Schema objects...],
  "themes": [Theme Schema objects...],
  "opportunities": [Opportunity Schema objects...],
  "data_gaps": [string],  // Missing information areas
  "research_limits": [string]  // Boundaries of the analysis
}
