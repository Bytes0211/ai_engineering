"""test_brochure.py

Unit tests for the brochure module.

Tests cover:
- BrochureGenerator initialization with valid/invalid API keys
- Link selection prompt building
- Link selection with mocked OpenAI responses
- Page content aggregation
- Brochure generation with mocked dependencies
- Streaming brochure generation

Author: scotton
Created: 2026-01-21
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
import os
import sys
from pathlib import Path

# Mock dependencies before importing brochure module
sys.modules['openai'] = MagicMock()
sys.modules['dotenv'] = MagicMock()
sys.modules['scraper'] = MagicMock()

# Add parent directory to path to import brochure module
sys.path.insert(0, str(Path(__file__).parent))
from brochure import BrochureGenerator, LINK_SYSTEM_PROMPT, BROCHURE_SYSTEM_PROMPT


class TestBrochureGeneratorInit(unittest.TestCase):
    """Tests for BrochureGenerator initialization."""
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"})
    @patch("brochure.OpenAI")
    def test_init_with_env_api_key(self, mock_openai):
        """Test initialization with API key from environment."""
        generator = BrochureGenerator()
        
        mock_openai.assert_called_once_with(api_key="sk-test-key")
        self.assertEqual(generator.link_selection_model, "gpt-5-nano")
        self.assertEqual(generator.brochure_model, "gpt-4.1-mini")
    
    @patch("brochure.OpenAI")
    def test_init_with_explicit_api_key(self, mock_openai):
        """Test initialization with explicitly provided API key."""
        generator = BrochureGenerator(api_key="sk-explicit-key")
        
        mock_openai.assert_called_once_with(api_key="sk-explicit-key")
    
    @patch.dict(os.environ, {}, clear=True)
    def test_init_without_api_key_raises_error(self):
        """Test that initialization fails without API key."""
        with self.assertRaises(ValueError) as context:
            BrochureGenerator()
        
        self.assertIn("OpenAI API key not found", str(context.exception))
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"})
    @patch("brochure.OpenAI")
    def test_init_with_custom_models(self, mock_openai):
        """Test initialization with custom model names."""
        generator = BrochureGenerator(
            link_selection_model="gpt-4.1-mini",
            brochure_model="gpt-5-nano"
        )
        
        self.assertEqual(generator.link_selection_model, "gpt-4.1-mini")
        self.assertEqual(generator.brochure_model, "gpt-5-nano")


class TestLinkSelection(unittest.TestCase):
    """Tests for link selection functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_client = Mock()
        self.mock_scraper = Mock()
        
        with patch("brochure.OpenAI", return_value=self.mock_client):
            with patch("brochure.Scraper", return_value=self.mock_scraper):
                self.generator = BrochureGenerator(api_key="sk-test-key")
    
    def test_get_links_user_prompt(self):
        """Test link selection user prompt generation."""
        self.mock_scraper.fetch_website_links.return_value = [
            "https://example.com/about",
            "/careers",
            "https://example.com/contact"
        ]
        
        prompt = self.generator._get_links_user_prompt("https://example.com")
        
        self.assertIn("https://example.com", prompt)
        self.assertIn("https://example.com/about", prompt)
        self.assertIn("/careers", prompt)
        self.assertIn("https://example.com/contact", prompt)
        self.assertIn("relevant web links for a brochure", prompt)
    
    def test_select_relevant_links(self):
        """Test link selection with mocked OpenAI response."""
        # Mock the scraper
        self.mock_scraper.fetch_website_links.return_value = [
            "https://example.com/about",
            "/careers",
            "https://example.com/privacy"
        ]
        
        # Mock OpenAI response
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        mock_message.content = json.dumps({
            "links": [
                {"type": "about page", "url": "https://example.com/about"},
                {"type": "careers page", "url": "https://example.com/careers"}
            ]
        })
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        self.mock_client.chat.completions.create.return_value = mock_response
        
        # Call the method
        with patch("builtins.print"):  # Suppress print output
            result = self.generator.select_relevant_links("https://example.com")
        
        # Verify the result
        self.assertIn("links", result)
        self.assertEqual(len(result["links"]), 2)
        self.assertEqual(result["links"][0]["type"], "about page")
        self.assertEqual(result["links"][1]["url"], "https://example.com/careers")
        
        # Verify OpenAI was called correctly
        self.mock_client.chat.completions.create.assert_called_once()
        call_args = self.mock_client.chat.completions.create.call_args
        self.assertEqual(call_args[1]["model"], "gpt-5-nano")
        self.assertEqual(call_args[1]["response_format"], {"type": "json_object"})


class TestPageContentAggregation(unittest.TestCase):
    """Tests for page content fetching and aggregation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_client = Mock()
        self.mock_scraper = Mock()
        
        with patch("brochure.OpenAI", return_value=self.mock_client):
            with patch("brochure.Scraper", return_value=self.mock_scraper):
                self.generator = BrochureGenerator(api_key="sk-test-key")
    
    def test_fetch_page_and_all_relevant_links(self):
        """Test fetching and aggregating content from multiple pages."""
        # Mock landing page content
        self.mock_scraper.fetch_website_contents.side_effect = [
            "Landing page content",
            "About page content",
            "Careers page content"
        ]
        
        # Mock link selection
        with patch.object(self.generator, "select_relevant_links") as mock_select:
            mock_select.return_value = {
                "links": [
                    {"type": "about page", "url": "https://example.com/about"},
                    {"type": "careers page", "url": "https://example.com/careers"}
                ]
            }
            
            result = self.generator.fetch_page_and_all_relevant_links("https://example.com")
        
        # Verify structure
        self.assertIn("## Landing Page:", result)
        self.assertIn("Landing page content", result)
        self.assertIn("## Relevant Links:", result)
        self.assertIn("### Link: about page", result)
        self.assertIn("About page content", result)
        self.assertIn("### Link: careers page", result)
        self.assertIn("Careers page content", result)
    
    def test_fetch_page_handles_errors(self):
        """Test that errors fetching linked pages are handled gracefully."""
        # Mock landing page success, but error on linked page
        self.mock_scraper.fetch_website_contents.side_effect = [
            "Landing page content",
            Exception("Network error")
        ]
        
        with patch.object(self.generator, "select_relevant_links") as mock_select:
            mock_select.return_value = {
                "links": [
                    {"type": "about page", "url": "https://example.com/about"}
                ]
            }
            
            result = self.generator.fetch_page_and_all_relevant_links("https://example.com")
        
        self.assertIn("Error fetching content: Network error", result)


class TestBrochureGeneration(unittest.TestCase):
    """Tests for brochure generation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_client = Mock()
        self.mock_scraper = Mock()
        
        with patch("brochure.OpenAI", return_value=self.mock_client):
            with patch("brochure.Scraper", return_value=self.mock_scraper):
                self.generator = BrochureGenerator(api_key="sk-test-key")
    
    def test_get_brochure_user_prompt(self):
        """Test brochure user prompt generation."""
        with patch.object(
            self.generator,
            "fetch_page_and_all_relevant_links"
        ) as mock_fetch:
            mock_fetch.return_value = "Aggregated content"
            
            prompt = self.generator._get_brochure_user_prompt(
                "TestCo",
                "https://example.com"
            )
        
        self.assertIn("TestCo", prompt)
        self.assertIn("Aggregated content", prompt)
        self.assertIn("landing page", prompt.lower())
    
    def test_get_brochure_user_prompt_truncates(self):
        """Test that brochure prompt is truncated at 5000 characters."""
        with patch.object(
            self.generator,
            "fetch_page_and_all_relevant_links"
        ) as mock_fetch:
            # Create content longer than 5000 characters
            mock_fetch.return_value = "x" * 10_000
            
            prompt = self.generator._get_brochure_user_prompt(
                "TestCo",
                "https://example.com"
            )
        
        self.assertLessEqual(len(prompt), 5_000)
    
    def test_create_brochure(self):
        """Test brochure generation with mocked dependencies."""
        # Mock the user prompt generation
        with patch.object(
            self.generator,
            "_get_brochure_user_prompt"
        ) as mock_prompt:
            mock_prompt.return_value = "Test prompt"
            
            # Mock OpenAI response
            mock_response = Mock()
            mock_choice = Mock()
            mock_message = Mock()
            mock_message.content = "# TestCo Brochure\n\nA great company!"
            mock_choice.message = mock_message
            mock_response.choices = [mock_choice]
            self.mock_client.chat.completions.create.return_value = mock_response
            
            # Generate brochure
            result = self.generator.create_brochure("TestCo", "https://example.com")
        
        # Verify result
        self.assertEqual(result, "# TestCo Brochure\n\nA great company!")
        
        # Verify OpenAI was called correctly
        call_args = self.mock_client.chat.completions.create.call_args
        self.assertEqual(call_args[1]["model"], "gpt-4.1-mini")
        messages = call_args[1]["messages"]
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[0]["content"], BROCHURE_SYSTEM_PROMPT)
        self.assertEqual(messages[1]["role"], "user")
    
    def test_stream_brochure(self):
        """Test streaming brochure generation."""
        # Mock the user prompt generation
        with patch.object(
            self.generator,
            "_get_brochure_user_prompt"
        ) as mock_prompt:
            mock_prompt.return_value = "Test prompt"
            
            # Mock streaming response
            mock_chunk1 = Mock()
            mock_chunk1.choices = [Mock()]
            mock_chunk1.choices[0].delta.content = "# TestCo"
            
            mock_chunk2 = Mock()
            mock_chunk2.choices = [Mock()]
            mock_chunk2.choices[0].delta.content = " Brochure"
            
            mock_chunk3 = Mock()
            mock_chunk3.choices = [Mock()]
            mock_chunk3.choices[0].delta.content = None  # End of stream
            
            self.mock_client.chat.completions.create.return_value = [
                mock_chunk1,
                mock_chunk2,
                mock_chunk3
            ]
            
            # Collect streamed chunks
            chunks = list(self.generator.stream_brochure("TestCo", "https://example.com"))
        
        # Verify chunks
        self.assertEqual(chunks, ["# TestCo", " Brochure"])
        
        # Verify OpenAI was called with stream=True
        call_args = self.mock_client.chat.completions.create.call_args
        self.assertTrue(call_args[1]["stream"])


class TestPromptConstants(unittest.TestCase):
    """Tests for prompt constant values."""
    
    def test_link_system_prompt_contains_key_elements(self):
        """Test that link system prompt has required instructions."""
        self.assertIn("relevant to include in a brochure", LINK_SYSTEM_PROMPT)
        self.assertIn("JSON", LINK_SYSTEM_PROMPT)
        self.assertIn("type", LINK_SYSTEM_PROMPT)
        self.assertIn("url", LINK_SYSTEM_PROMPT)
    
    def test_brochure_system_prompt_contains_key_elements(self):
        """Test that brochure system prompt has required instructions."""
        self.assertIn("brochure", BROCHURE_SYSTEM_PROMPT)
        self.assertIn("markdown", BROCHURE_SYSTEM_PROMPT)
        self.assertIn("prospective customers", BROCHURE_SYSTEM_PROMPT)
        self.assertIn("company culture", BROCHURE_SYSTEM_PROMPT)


if __name__ == "__main__":
    unittest.main()
