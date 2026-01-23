"""Unit tests for tokens.py module.

Tests tokenization functions (no API calls required).
"""

import unittest
from unittest.mock import patch

import tiktoken

from tokens import (
    decode_tokens,
    encode_text,
    get_encoding_for_model,
    print_tokens_breakdown,
)


class TestTokenization(unittest.TestCase):
    """Test tokenization functions."""
    
    def test_get_encoding_for_model(self):
        """Test getting encoding for a model."""
        encoding = get_encoding_for_model("gpt-4.1-mini")
        self.assertIsInstance(encoding, tiktoken.Encoding)
    
    def test_encode_text(self):
        """Test encoding text into tokens."""
        text = "Hello world"
        tokens = encode_text(text)
        self.assertIsInstance(tokens, list)
        self.assertTrue(len(tokens) > 0)
        self.assertTrue(all(isinstance(t, int) for t in tokens))
    
    def test_decode_tokens(self):
        """Test decoding tokens back to text."""
        text = "Hello world"
        tokens = encode_text(text)
        decoded = decode_tokens(tokens)
        self.assertEqual(decoded, text)
    
    def test_encode_decode_roundtrip(self):
        """Test that encoding and decoding preserves text."""
        original = "Hi my name is Ed and I like banoffee pie"
        tokens = encode_text(original)
        decoded = decode_tokens(tokens)
        self.assertEqual(decoded, original)
    
    def test_specific_token_decode(self):
        """Test decoding a specific token ID."""
        # Token 326 should decode to something (exact value may vary by model)
        decoded = decode_tokens([326])
        self.assertIsInstance(decoded, str)
    
    @patch('builtins.print')
    def test_print_tokens_breakdown(self, mock_print):
        """Test printing token breakdown."""
        text = "Hi there"
        print_tokens_breakdown(text)
        # Should print at least the text and total tokens
        self.assertTrue(mock_print.called)
        # Check that we printed something about the text
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("Hi there" in str(call) for call in calls))



if __name__ == "__main__":
    unittest.main()
