"""Unit tests for memory_illusion.py module.

Tests conversation memory demonstration with mocking to avoid API calls.
"""

import os
import unittest
from unittest.mock import MagicMock, patch

from memory_illusion import demonstrate_stateless_conversation, validate_api_key


class TestAPIKeyValidation(unittest.TestCase):
    """Test API key validation."""
    
    @patch.dict(os.environ, {}, clear=True)
    @patch('memory_illusion.load_dotenv')
    @patch('builtins.print')
    def test_validate_api_key_missing(self, mock_print, mock_load_dotenv):
        """Test validation when API key is missing."""
        with patch('os.getenv', return_value=None):
            result = validate_api_key()
            self.assertIsNone(result)
            mock_print.assert_called_once()
            self.assertIn("No API key", str(mock_print.call_args))
    
    @patch('memory_illusion.load_dotenv')
    @patch('builtins.print')
    def test_validate_api_key_invalid_format(self, mock_print, mock_load_dotenv):
        """Test validation when API key has wrong format."""
        with patch('os.getenv', return_value='sk-invalid-key'):
            result = validate_api_key()
            self.assertEqual(result, 'sk-invalid-key')
            mock_print.assert_called_once()
            self.assertIn("doesn't start with sk-proj-", str(mock_print.call_args))
    
    @patch('memory_illusion.load_dotenv')
    @patch('builtins.print')
    def test_validate_api_key_valid(self, mock_print, mock_load_dotenv):
        """Test validation when API key is valid."""
        with patch('os.getenv', return_value='sk-proj-valid-key-here'):
            result = validate_api_key()
            self.assertEqual(result, 'sk-proj-valid-key-here')
            mock_print.assert_called_once()
            self.assertIn("looks good", str(mock_print.call_args))


class TestConversationDemo(unittest.TestCase):
    """Test conversation demonstration function."""
    
    @patch('memory_illusion.validate_api_key')
    @patch('memory_illusion.OpenAI')
    @patch('builtins.print')
    def test_demonstrate_stateless_conversation(
        self, mock_print, mock_openai_class, mock_validate
    ):
        """Test the conversation demonstration with mocked API calls."""
        # Mock API key validation
        mock_validate.return_value = 'sk-proj-test-key'
        
        # Mock OpenAI client and response
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Mocked response"
        mock_client.chat.completions.create.return_value = mock_response
        
        demonstrate_stateless_conversation()
        
        # Verify OpenAI client was called 3 times (3 demonstrations)
        self.assertEqual(mock_client.chat.completions.create.call_count, 3)
        
        # Verify key takeaway was printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("stateless" in str(call).lower() for call in print_calls)
        )
    
    @patch('memory_illusion.validate_api_key')
    @patch('builtins.print')
    def test_demonstrate_stateless_conversation_no_api_key(
        self, mock_print, mock_validate
    ):
        """Test conversation demo exits gracefully without API key."""
        mock_validate.return_value = None
        
        demonstrate_stateless_conversation()
        
        # Should return early, not make any API calls
    
    @patch('memory_illusion.validate_api_key')
    @patch('memory_illusion.OpenAI')
    @patch('builtins.print')
    def test_conversation_messages_structure(
        self, mock_print, mock_openai_class, mock_validate
    ):
        """Test that conversation messages have correct structure."""
        mock_validate.return_value = 'sk-proj-test-key'
        
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Mocked response"
        mock_client.chat.completions.create.return_value = mock_response
        
        demonstrate_stateless_conversation()
        
        # Get all calls to the API
        calls = mock_client.chat.completions.create.call_args_list
        
        # First call should have 2 messages (system + user intro)
        first_call_messages = calls[0].kwargs['messages']
        self.assertEqual(len(first_call_messages), 2)
        self.assertEqual(first_call_messages[0]['role'], 'system')
        self.assertEqual(first_call_messages[1]['role'], 'user')
        
        # Second call should have 2 messages (system + user question, NO history)
        second_call_messages = calls[1].kwargs['messages']
        self.assertEqual(len(second_call_messages), 2)
        
        # Third call should have 4 messages (with conversation history)
        third_call_messages = calls[2].kwargs['messages']
        self.assertEqual(len(third_call_messages), 4)
        self.assertEqual(third_call_messages[2]['role'], 'assistant')


if __name__ == "__main__":
    unittest.main()
