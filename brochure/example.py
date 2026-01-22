#!/usr/bin/env python3
"""example.py

Example usage of the BrochureGenerator.

This script demonstrates how to use the brochure generator to create
professional company brochures from website content.

Author: scotton
Created: 2026-01-21
"""

import sys
from pathlib import Path

# Add parent directory to path to import brochure module
sys.path.insert(0, str(Path(__file__).parent.parent / "agent"))

from brochure import BrochureGenerator


def example_basic_usage():
    """Basic example: Generate a brochure."""
    print("=" * 70)
    print("Example 1: Basic Brochure Generation")
    print("=" * 70)
    
    generator = BrochureGenerator()
    brochure = generator.create_brochure(
        "HuggingFace",
        "https://huggingface.co"
    )
    
    print("\n# Generated Brochure\n")
    print(brochure)
    print("\n")


def example_streaming():
    """Example: Stream brochure generation."""
    print("=" * 70)
    print("Example 2: Streaming Brochure Generation")
    print("=" * 70)
    
    generator = BrochureGenerator()
    
    print("\n# Streaming Brochure\n")
    for chunk in generator.stream_brochure(
        "OpenAI",
        "https://openai.com"
    ):
        print(chunk, end="", flush=True)
    print("\n")


def example_custom_models():
    """Example: Use custom models."""
    print("=" * 70)
    print("Example 3: Custom Model Configuration")
    print("=" * 70)
    
    generator = BrochureGenerator(
        link_selection_model="gpt-4.1-mini",
        brochure_model="gpt-5-nano"
    )
    
    brochure = generator.create_brochure(
        "Anthropic",
        "https://anthropic.com"
    )
    
    print("\n# Generated Brochure (with custom models)\n")
    print(brochure)
    print("\n")


def example_link_selection():
    """Example: Just select relevant links."""
    print("=" * 70)
    print("Example 4: Link Selection Only")
    print("=" * 70)
    
    generator = BrochureGenerator()
    
    print("\nSelecting relevant links from website...")
    links = generator.select_relevant_links("https://edwarddonner.com")
    
    print("\nSelected Links:")
    for link_info in links.get("links", []):
        print(f"  - {link_info['type']}: {link_info['url']}")
    print("\n")


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("BROCHURE GENERATOR EXAMPLES")
    print("=" * 70 + "\n")
    
    # Choose which examples to run
    # Uncomment the examples you want to execute
    
    # Note: These examples make real API calls and will incur costs
    # Make sure you have OPENAI_API_KEY set in your .env file
    
    # example_basic_usage()
    # example_streaming()
    # example_custom_models()
    # example_link_selection()
    
    print("\nTo run examples, uncomment the function calls in main()")
    print("Note: Examples make real API calls and will incur costs\n")


if __name__ == "__main__":
    main()
