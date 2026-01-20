#!/usr/bin/env python3
"""
Unit tests for the Agent class.

Tests cover initialization, prompt customization, language support,
and integration with the Scraper class.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from agent import Agent


class TestAgentInitialization(unittest.TestCase):
    """Test Agent initialization and attribute setup."""
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_default_initialization(self, mock_dotenv, mock_openai):
        """Test agent initializes with default values."""
        agent = Agent("TestAgent")
        
        self.assertEqual(agent.name, "TestAgent")
        self.assertEqual(agent.language, "English")
        self.assertIn("assistant", agent.system_prompt)
        self.assertIn("English", agent.system_prompt)
        mock_dotenv.assert_called_once_with(override=True)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_custom_role_initialization(self, mock_dotenv, mock_openai):
        """Test agent initializes with custom role."""
        agent = Agent("TestAgent", role="expert analyst")
        
        self.assertIn("expert analyst", agent.system_prompt)
        self.assertIn("English", agent.system_prompt)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_custom_language_initialization(self, mock_dotenv, mock_openai):
        """Test agent initializes with custom language."""
        agent = Agent("TestAgent", language="Spanish")
        
        self.assertEqual(agent.language, "Spanish")
        self.assertIn("Spanish", agent.system_prompt)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_custom_role_and_language_initialization(self, mock_dotenv, mock_openai):
        """Test agent initializes with custom role and language."""
        agent = Agent("TestAgent", role="rapper", language="French")
        
        self.assertEqual(agent.language, "French")
        self.assertIn("rapper", agent.system_prompt)
        self.assertIn("French", agent.system_prompt)


class TestAgentPromptCustomization(unittest.TestCase):
    """Test prompt customization methods."""
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_set_role(self, mock_dotenv, mock_openai):
        """Test changing the role updates the system prompt."""
        agent = Agent("TestAgent")
        agent.set_role("comedian")
        
        self.assertIn("comedian", agent.system_prompt)
        self.assertIn(agent.language, agent.system_prompt)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_set_language(self, mock_dotenv, mock_openai):
        """Test changing the language updates the system prompt."""
        agent = Agent("TestAgent")
        agent.set_language("German")
        
        self.assertEqual(agent.language, "German")
        self.assertIn("German", agent.system_prompt)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_set_system_prompt(self, mock_dotenv, mock_openai):
        """Test setting a custom system prompt."""
        agent = Agent("TestAgent")
        custom_prompt = "You are a professional analyst."
        agent.set_system_prompt(custom_prompt)
        
        self.assertEqual(agent.system_prompt, custom_prompt)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_set_user_prompt_prefix(self, mock_dotenv, mock_openai):
        """Test setting a custom user prompt prefix."""
        agent = Agent("TestAgent")
        custom_prefix = "Analyze this content: "
        agent.set_user_prompt_prefix(custom_prefix)
        
        self.assertEqual(agent.user_prompt_prefix, custom_prefix)


class TestAgentMessaging(unittest.TestCase):
    """Test message building for OpenAI API."""
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_messages_for(self, mock_dotenv, mock_openai):
        """Test message array construction."""
        agent = Agent("TestAgent")
        website_content = "Test website content"
        
        messages = agent.messages_for(website_content)
        
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[0]["content"], agent.system_prompt)
        self.assertEqual(messages[1]["role"], "user")
        self.assertIn(website_content, messages[1]["content"])


class TestAgentSummarization(unittest.TestCase):
    """Test website summarization functionality."""
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_summarize_integration(self, mock_dotenv, mock_openai):
        """Test summarize method calls scraper and OpenAI API."""
        # Setup mocks
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Test summary"
        mock_client.chat.completions.create.return_value = mock_response
        
        # Create agent and mock scraper
        agent = Agent("TestAgent")
        agent.scraper.fetch_website_contents = Mock(return_value="Website content")
        
        # Test summarize
        result = agent.summarize("https://example.com")
        
        # Verify calls
        agent.scraper.fetch_website_contents.assert_called_once_with("https://example.com")
        mock_client.chat.completions.create.assert_called_once()
        self.assertEqual(result, "Test summary")
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_summarize_with_custom_model(self, mock_dotenv, mock_openai):
        """Test summarize method with custom model."""
        # Setup mocks
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Test summary"
        mock_client.chat.completions.create.return_value = mock_response
        
        # Create agent and mock scraper
        agent = Agent("TestAgent")
        agent.scraper.fetch_website_contents = Mock(return_value="Website content")
        
        # Test summarize with custom model
        result = agent.summarize("https://example.com", model="gpt-4")
        
        # Verify model was passed
        call_args = mock_client.chat.completions.create.call_args
        self.assertEqual(call_args.kwargs["model"], "gpt-4")


class TestLanguageFeature(unittest.TestCase):
    """Test language-specific functionality."""
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_language_persists_after_role_change(self, mock_dotenv, mock_openai):
        """Test language is preserved when changing roles."""
        agent = Agent("TestAgent", language="Spanish")
        agent.set_role("expert analyst")
        
        self.assertEqual(agent.language, "Spanish")
        self.assertIn("Spanish", agent.system_prompt)
        self.assertIn("expert analyst", agent.system_prompt)
    
    @patch('agent.OpenAI')
    @patch('agent.load_dotenv')
    def test_multiple_language_changes(self, mock_dotenv, mock_openai):
        """Test multiple language changes update correctly."""
        agent = Agent("TestAgent")
        
        languages = ["Spanish", "French", "German", "Japanese"]
        for lang in languages:
            agent.set_language(lang)
            self.assertEqual(agent.language, lang)
            self.assertIn(lang, agent.system_prompt)


if __name__ == "__main__":
    unittest.main()
