"""test_prompt_generator.py

Unit tests for the prompt_generator module.

Tests the core functionality of loading templates, generating prompts,
and validating JSON output structure.

Author: scotton
Created: 2026-01-23
"""

import json
import unittest
from pathlib import Path
from unittest.mock import patch, mock_open
from prompt_generator import (
    load_prompt_templates,
    display_prompt_menu,
    get_user_selection,
    get_user_content,
    generate_prompt_json
)


class TestPromptGenerator(unittest.TestCase):
    """Test cases for prompt generator functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_templates = {
            "prompts": [
                {
                    "id": 1,
                    "name": "Test Template",
                    "description": "A test template",
                    "default_content": "Test content",
                    "system_prompt": "You are a test assistant.",
                    "developer_prompt": "Test developer instructions.",
                    "user_prompt_template": "Process this: {content}"
                },
                {
                    "id": 2,
                    "name": "Second Template",
                    "description": "Another test template",
                    "default_content": "More test content",
                    "system_prompt": "You are another assistant.",
                    "developer_prompt": "More developer instructions.",
                    "user_prompt_template": "Handle this: {content}"
                }
            ]
        }
    
    def test_load_templates_success(self):
        """Test loading templates from a valid JSON file."""
        mock_json = json.dumps(self.sample_templates)
        
        with patch('pathlib.Path.exists', return_value=True):
            with patch('builtins.open', mock_open(read_data=mock_json)):
                templates = load_prompt_templates("test.json")
                
        self.assertIn("prompts", templates)
        self.assertEqual(len(templates["prompts"]), 2)
        self.assertEqual(templates["prompts"][0]["name"], "Test Template")
    
    def test_load_templates_file_not_found(self):
        """Test error handling when template file doesn't exist."""
        with patch('pathlib.Path.exists', return_value=False):
            with self.assertRaises(FileNotFoundError):
                load_prompt_templates("nonexistent.json")
    
    def test_load_templates_invalid_json(self):
        """Test error handling for invalid JSON."""
        with patch('pathlib.Path.exists', return_value=True):
            with patch('builtins.open', mock_open(read_data="invalid json {")):
                with self.assertRaises(json.JSONDecodeError):
                    load_prompt_templates("invalid.json")
    
    def test_display_prompt_menu(self):
        """Test that menu displays without errors."""
        # This test just verifies no exceptions are raised
        with patch('builtins.print') as mock_print:
            display_prompt_menu(self.sample_templates)
            
        # Verify print was called (menu was displayed)
        self.assertTrue(mock_print.called)
        
        # Check that template names were printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("Test Template" in str(call) for call in print_calls))
    
    @patch('builtins.input', side_effect=['1'])
    def test_get_user_selection_valid(self, mock_input):
        """Test valid user selection."""
        choice = get_user_selection(2)
        self.assertEqual(choice, 1)
    
    @patch('builtins.input', side_effect=['0', '3', '2'])
    def test_get_user_selection_invalid_then_valid(self, mock_input):
        """Test handling of invalid input followed by valid input."""
        with patch('builtins.print'):
            choice = get_user_selection(2)
        self.assertEqual(choice, 2)
    
    @patch('builtins.input', side_effect=['abc', '1'])
    def test_get_user_selection_non_numeric(self, mock_input):
        """Test handling of non-numeric input."""
        with patch('builtins.print'):
            choice = get_user_selection(2)
        self.assertEqual(choice, 1)
    
    @patch('builtins.input', side_effect=['y'])
    def test_get_user_content_use_default(self, mock_input):
        """Test using default content."""
        template = self.sample_templates["prompts"][0]
        with patch('builtins.print'):
            content = get_user_content(template)
        self.assertEqual(content, "Test content")
    
    @patch('builtins.input', side_effect=['n', 'Custom content', '', ''])
    def test_get_user_content_custom(self, mock_input):
        """Test entering custom content."""
        template = self.sample_templates["prompts"][0]
        with patch('builtins.print'):
            content = get_user_content(template)
        self.assertEqual(content, "Custom content")
    
    @patch('builtins.input', side_effect=['n', 'Line 1', 'Line 2', '', ''])
    def test_get_user_content_multiline(self, mock_input):
        """Test entering multi-line content."""
        template = self.sample_templates["prompts"][0]
        with patch('builtins.print'):
            content = get_user_content(template)
        self.assertEqual(content, "Line 1\nLine 2")
    
    @patch('builtins.input', side_effect=['n', '', ''])
    def test_get_user_content_empty_uses_default(self, mock_input):
        """Test that empty content falls back to default."""
        template = self.sample_templates["prompts"][0]
        with patch('builtins.print'):
            content = get_user_content(template)
        self.assertEqual(content, "Test content")
    
    def test_generate_prompt_json_structure(self):
        """Test that generated JSON has correct structure."""
        template = self.sample_templates["prompts"][0]
        content = "My test content"
        
        json_output = generate_prompt_json(template, content)
        messages = json.loads(json_output)
        
        # Check structure
        self.assertEqual(len(messages), 3)
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["role"], "developer")
        self.assertEqual(messages[2]["role"], "user")
        
        # Check content
        self.assertEqual(messages[0]["content"], "You are a test assistant.")
        self.assertEqual(messages[1]["content"], "Test developer instructions.")
        self.assertEqual(messages[2]["content"], "Process this: My test content")
    
    def test_generate_prompt_json_content_substitution(self):
        """Test that content is properly substituted in template."""
        template = self.sample_templates["prompts"][1]
        content = "Special test content"
        
        json_output = generate_prompt_json(template, content)
        messages = json.loads(json_output)
        
        self.assertIn("Special test content", messages[2]["content"])
        self.assertEqual(messages[2]["content"], "Handle this: Special test content")
    
    def test_generate_prompt_json_valid_json(self):
        """Test that generated output is valid JSON."""
        template = self.sample_templates["prompts"][0]
        content = "Test"
        
        json_output = generate_prompt_json(template, content)
        
        # Should not raise an exception
        try:
            json.loads(json_output)
        except json.JSONDecodeError:
            self.fail("Generated output is not valid JSON")
    
    def test_generate_prompt_json_special_characters(self):
        """Test handling of special characters in content."""
        template = self.sample_templates["prompts"][0]
        content = 'Content with "quotes" and \n newlines'
        
        json_output = generate_prompt_json(template, content)
        messages = json.loads(json_output)
        
        # Verify special characters are properly escaped
        self.assertIn("quotes", messages[2]["content"])
        self.assertIn("newlines", messages[2]["content"])


class TestTemplateIntegration(unittest.TestCase):
    """Integration tests using actual template file."""
    
    def test_load_actual_template_file(self):
        """Test loading the actual prompt_templates.json file."""
        template_path = Path("prompt_templates.json")
        
        if not template_path.exists():
            self.skipTest("prompt_templates.json not found")
        
        templates = load_prompt_templates("prompt_templates.json")
        
        # Verify structure
        self.assertIn("prompts", templates)
        self.assertIsInstance(templates["prompts"], list)
        self.assertGreater(len(templates["prompts"]), 0)
        
        # Verify each template has required fields
        required_fields = [
            "id", "name", "description", "default_content",
            "system_prompt", "developer_prompt", "user_prompt_template"
        ]
        
        for prompt in templates["prompts"]:
            for field in required_fields:
                self.assertIn(field, prompt, 
                            f"Template '{prompt.get('name', 'unknown')}' missing field: {field}")
    
    def test_all_templates_generate_valid_json(self):
        """Test that all templates generate valid JSON."""
        template_path = Path("prompt_templates.json")
        
        if not template_path.exists():
            self.skipTest("prompt_templates.json not found")
        
        templates = load_prompt_templates("prompt_templates.json")
        
        for template in templates["prompts"]:
            with self.subTest(template=template["name"]):
                json_output = generate_prompt_json(template, "Test content")
                
                # Should parse without error
                messages = json.loads(json_output)
                
                # Verify structure
                self.assertEqual(len(messages), 3)
                self.assertEqual(messages[0]["role"], "system")
                self.assertEqual(messages[1]["role"], "developer")
                self.assertEqual(messages[2]["role"], "user")


if __name__ == "__main__":
    unittest.main()
