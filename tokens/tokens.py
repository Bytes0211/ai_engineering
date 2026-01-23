# Auto-Generated
# File Name: tokens.py 
# Author: scotton
# Creation Date: January-22-2026
# Modified Date: January-22-2026

"""Token encoding and decoding for GPT models.

This module provides functions for tokenizing text using tiktoken,
which is essential for understanding API costs and context limits.

Based on week1/day4.ipynb
"""

import tiktoken


def get_encoding_for_model(model: str = "gpt-4.1-mini") -> tiktoken.Encoding:
    """Get the tiktoken encoding for a specific model.
    
    Args:
        model: The model name to get encoding for (default: gpt-4.1-mini)
        
    Returns:
        A tiktoken Encoding object for the specified model
    """
    return tiktoken.encoding_for_model(model)


def encode_text(text: str, model: str = "gpt-4.1-mini") -> list[int]:
    """Encode text into tokens for a specific model.
    
    Args:
        text: The text to encode
        model: The model name to use for encoding (default: gpt-4.1-mini)
        
    Returns:
        A list of token IDs
    """
    encoding = get_encoding_for_model(model)
    return encoding.encode(text)


def decode_tokens(tokens: list[int], model: str = "gpt-4.1-mini") -> str:
    """Decode a list of token IDs back into text.
    
    Args:
        tokens: List of token IDs to decode
        model: The model name used for encoding (default: gpt-4.1-mini)
        
    Returns:
        The decoded text string
    """
    encoding = get_encoding_for_model(model)
    return encoding.decode(tokens)


def print_tokens_breakdown(text: str, model: str = "gpt-4.1-mini") -> None:
    """Print a breakdown of how text is tokenized.
    
    Shows each token ID and its corresponding text.
    
    Args:
        text: The text to tokenize and display
        model: The model name to use for encoding (default: gpt-4.1-mini)
    """
    encoding = get_encoding_for_model(model)
    tokens = encoding.encode(text)
    
    print(f"Text: {text}")
    print(f"Total tokens: {len(tokens)}\n")
    
    for token_id in tokens:
        token_text = encoding.decode([token_id])
        print(f"{token_id} = {repr(token_text)}")



def main() -> None:
    """Main function demonstrating tokenization."""
    print("=== Tokenization Demo ===\n")
    text = "Hi! My name is Steven and I love coffee!"
    print_tokens_breakdown(text)
    
    # Decode a specific token
    print("\nDecoding token 326:")
    print(f"Token 326 = {decode_tokens([326])}")
    
    print("\n" + "="*50)
    print("\nNote: For conversation memory demonstration, run:")
    print("  uv run python memory_illusion.py")


if __name__ == "__main__":
    main()



