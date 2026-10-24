#!/usr/bin/env python3
"""
Minimal validation script for the skill structure.
"""

import os
import json

def validate_structure():
    """Basic validation of required files and structure."""
    print("🔍 Validating Competitor Review Mining Skill Structure")
    
    # Check directories
    required_dirs = ["references", "scripts", "evals", "evals/data", "outputs"]
    dir_check = all(os.path.exists(d) for d in required_dirs)
    print("Directories:", "✅ All present" if dir_check else "❌ Missing some")
    
    # Check required files
    required_files = [
        "SKILL.md",
        "references/source-matrix.md", 
        "references/analysis-framework.md",
        "scripts/collect_reviews.py",
        "references/schemas.md"
    ]
    file_check = all(os.path.exists(f) for f in required_files)
    print("Files:", "✅ All present" if file_check else "❌ Some missing")
    
    # Check git repo
    git_check = os.path.exists(".git")
    print("Git repo:", "✅ Initialized" if git_check else "❌ Not initialized")
    
    # Check basic Python imports
    try:
        import json
        print("✅ Basic Python imports work")
        imports_ok = True
    except ImportError:
        imports_ok = False
        print("❌ Python import failed")
    
    # Summary
    overall_check = dir_check and file_check and git_check and imports_ok
    print(f"\n{'✅ STRUCTURE VALID' if overall_check else '❌ STRUCTURE INCOMPLETE'}")
    return overall_check

if __name__ == "__main__":
    exit(0 if validate_structure() else 1)
