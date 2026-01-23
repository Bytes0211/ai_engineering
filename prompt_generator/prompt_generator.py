"""prompt_generator.py

Interactive prompt generator for various business communication scenarios.

This module provides an interactive CLI to:
1. Display available prompt templates
2. Allow user to select a template
3. Select an LLM model
4. Collect user content
5. Send to OpenRouter API and get response

Based on prompt_templates.json structure.

Author: scotton
Created: 2026-01-23
"""

import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Please install it: uv add requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: 'python-dotenv' library not found. Please install it: uv add python-dotenv")
    sys.exit(1)


def load_prompt_templates(filepath: str = "prompt_templates.json") -> dict:
    """Load prompt templates from JSON file.
    
    Args:
        filepath: Path to the JSON file containing prompt templates
        
    Returns:
        Dictionary containing prompt templates
        
    Raises:
        FileNotFoundError: If the template file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Template file not found: {filepath}")
    
    with open(path, 'r') as f:
        return json.load(f)


def display_prompt_menu(templates: dict) -> None:
    """Display available prompt templates.
    
    Args:
        templates: Dictionary containing prompt templates
    """
    print("\n" + "=" * 70)
    print("Available Prompt Templates")
    print("=" * 70)
    print()
    
    for prompt in templates["prompts"]:
        print(f"{prompt['id']:2d}. {prompt['name']}")
        print(f"    {prompt['description']}")
        print()


def get_user_selection(max_choice: int) -> int:
    """Get and validate user's prompt selection.
    
    Args:
        max_choice: Maximum valid choice number
        
    Returns:
        Valid prompt ID selected by user
    """
    while True:
        try:
            choice = input(f"Select a prompt (1-{max_choice}): ").strip()
            choice_num = int(choice)
            
            if 1 <= choice_num <= max_choice:
                return choice_num
            else:
                print(f"Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)


def get_model_selection() -> str:
    """Prompt user to select an LLM model.
    
    Returns:
        Selected model identifier for OpenRouter
    """
    models = {
        1: {"name": "GPT-4.1 Mini", "id": "openai/gpt-4.1-mini"},
        2: {"name": "Claude 3.5 Haiku", "id": "anthropic/claude-3.5-haiku"}
    }
    
    print("\n" + "=" * 70)
    print("Select Model")
    print("=" * 70)
    print()
    
    for key, model in models.items():
        print(f"{key}. {model['name']}")
    print()
    
    while True:
        try:
            choice = input("Select a model (1-2): ").strip()
            choice_num = int(choice)
            
            if choice_num in models:
                selected = models[choice_num]
                print(f"\n✓ Selected: {selected['name']}")
                return selected["id"]
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)


def get_user_content(prompt_template: dict) -> str:
    """Get content from user with option to use default.
    
    Args:
        prompt_template: The selected prompt template dictionary
        
    Returns:
        User-provided content or default content
    """
    print(f"\nDefault content: {prompt_template['default_content']}")
    print()
    
    use_default = input("Use default content? (y/n) [n]: ").strip().lower()
    
    if use_default in ['y', 'yes']:
        return prompt_template['default_content']
    
    print("\nEnter your content (press Enter twice when done):")
    lines = []
    empty_line_count = 0
    
    while True:
        try:
            line = input()
            if line == "":
                empty_line_count += 1
                if empty_line_count >= 2:
                    break
            else:
                empty_line_count = 0
            lines.append(line)
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
    
    # Remove trailing empty lines
    while lines and lines[-1] == "":
        lines.pop()
    
    content = "\n".join(lines).strip()
    
    if not content:
        print("\nNo content provided. Using default.")
        return prompt_template['default_content']
    
    return content


def build_messages(prompt_template: dict, content: str) -> list:
    """Build message list for LLM API.
    
    Args:
        prompt_template: The selected prompt template dictionary
        content: User-provided content
        
    Returns:
        List of message dictionaries
    """
    return [
        {
            "role": "system",
            "content": prompt_template["system_prompt"]
        },
        {
            "role": "developer",
            "content": prompt_template["developer_prompt"]
        },
        {
            "role": "user",
            "content": prompt_template["user_prompt_template"].format(content=content)
        }
    ]


def send_to_openrouter(messages: list, model: str, api_key: str) -> str:
    """Send messages to OpenRouter API and get response.
    
    Args:
        messages: List of message dictionaries
        model: Model identifier for OpenRouter
        api_key: OpenRouter API key
        
    Returns:
        Response content from the LLM
        
    Raises:
        requests.RequestException: If API request fails
    """
    # Convert developer role to system for compatibility
    formatted_messages = []
    system_parts = []
    
    for msg in messages:
        if msg["role"] in ["system", "developer"]:
            system_parts.append(msg["content"])
        else:
            formatted_messages.append(msg)
    
    # Combine system and developer prompts
    if system_parts:
        formatted_messages.insert(0, {
            "role": "system",
            "content": "\n\n".join(system_parts)
        })
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/scotton/ai_engineering",
            "X-Title": "Prompt Generator CLI"
        },
        json={
            "model": model,
            "messages": formatted_messages
        },
        timeout=30
    )
    
    response.raise_for_status()
    result = response.json()
    
    return result["choices"][0]["message"]["content"]


def main():
    """Interactive prompt generator CLI."""
    try:
        # Load environment variables
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        
        if not api_key:
            print("Error: OPENROUTER_API_KEY not found in environment.")
            print("Please set it in your .env file or environment variables.")
            sys.exit(1)
        
        # Load templates
        templates = load_prompt_templates()
        
        # Display menu
        display_prompt_menu(templates)
        
        # Get user selection
        max_choice = len(templates["prompts"])
        selected_id = get_user_selection(max_choice)
        
        # Find selected template
        selected_template = next(
            (p for p in templates["prompts"] if p["id"] == selected_id),
            None
        )
        
        if not selected_template:
            print(f"Error: Could not find template with ID {selected_id}")
            sys.exit(1)
        
        print(f"\n✓ Selected: {selected_template['name']}")
        
        # Get model selection
        model = get_model_selection()
        
        # Get content from user
        content = get_user_content(selected_template)
        
        # Display confirmation
        print("\n" + "=" * 70)
        print("Content Accepted")
        print("=" * 70)
        print()
        print(content)
        print()
        
        # Build messages
        messages = build_messages(selected_template, content)
        
        # Send to API
        print("=" * 70)
        print(f"Generating response with {model.split('/')[-1]}...")
        print("=" * 70)
        print()
        
        response = send_to_openrouter(messages, model, api_key)
        
        # Display response
        print("\n" + "=" * 70)
        print("Response")
        print("=" * 70)
        print()
        print(response)
        print()
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in template file: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Error: API request failed: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
