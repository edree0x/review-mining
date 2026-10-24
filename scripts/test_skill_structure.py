#!/usr/bin/env python3
"""
Test script to validate the competitor review mining skill structure.
"""

import os
import sys
import json

def test_directory_structure():
    """Validate that all required directories exist."""
    required_dirs = [
        "references",
        "scripts", 
        "evals",
        "evals/data",
        "outputs"
    ]
    
    success = True
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            print(f"❌ Missing directory: {dir_name}")
            success = False
        else:
            print(f"✅ Directory exists: {dir_name}")
    
    return success

def test_required_files():
    """Validate that required files exist."""
    required_files = [
        "SKILL.md",
        "references/source-matrix.md",
        "references/analysis-framework.md",
        "references/schemas.md",
        "scripts/collect_reviews.py",
        "scripts/analyze_themes.py", 
        "scripts/export_xlsx.py",
        "evals/evals.json"
    ]
    
    success = True
    for file_name in required_files:
        if not os.path.exists(file_name):
            print(f"❌ Missing file: {file_name}")
            success = False
        else:
            print(f"✅ File exists: {file_name}")
    
    return success

def test_git_repo_initialization():
    """Validate that git repo is initialized."""
    if os.path.exists(".git"):
        print("✅ Git repository initialized")
        return True
    else:
        print("❌ Git repository not initialized")
        return False

def check_importability():
    """Test that scripts can be imported without errors."""
    try:
        # Test import of main scripts
        sys.path.insert(0, "scripts")
        import collect_reviews
        import analyze_themes
        import export_xlsx
        print("✅ Script imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    finally:
        if "scripts" in sys.path:
            sys.path.pop(0)

def main():
    """Run all validation checks."""
    print("🔍 Validating Competitor Review Mining Skill Structure")
    print("=" * 50)
    
    checks = [
        ("Directory Structure", test_directory_structure),
        ("Required Files", test_required_files), 
        ("Git Initialization", test_git_repo_initialization),
        ("Script Importability", check_importability)
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        result = check_func()
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL VALIDATIONS PASSED")
        return 0
    else:
        print("💥 SOME VALIDATIONS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
