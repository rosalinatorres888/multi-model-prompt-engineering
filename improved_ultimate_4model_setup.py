#!/usr/bin/env python3
"""
IMPROVED ULTIMATE 4-MODEL AI SETUP FOR PROMPT ENGINEERING
==========================================================

Enhanced version with:
- Multiple Google API keys with automatic rotation
- Different Gemini model names (gemini-1.5-pro, gemini-pro)
- Improved error handling and model compatibility
- Better Llama API handling

The most comprehensive prompt engineering platform with access to:
- OpenAI GPT-4 & GPT-3.5
- Meta Llama models  
- Google Gemini (with multiple keys and model versions)
- Anthropic Claude (Sonnet & Haiku)
"""

import os
import sys
import requests
import json
from typing import Dict, Optional, List, Any

# Install and import required libraries
def ensure_package(package_name, import_name=None):
    """Ensure a package is installed and import it"""
    import_name = import_name or package_name
    try:
        __import__(import_name)
        return True
    except ImportError:
        print(f"📦 Installing {package_name}...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return True

# Ensure required packages
required_packages = [
    ('python-dotenv', 'dotenv'),
    ('openai', 'openai'),
    ('google-generativeai', 'google.generativeai'),
    ('anthropic', 'anthropic'),
    ('requests', 'requests')
]

print("🔧 Checking required packages...")
for package, import_name in required_packages:
    ensure_package(package, import_name)

# Now import everything
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()


class ImprovedUltimate4ModelPlatform:
    """Improved ultimate 4-model prompt engineering platform"""
    
    def __init__(self):
        """Initialize with all 4 major AI providers + improved Google handling"""
        
        print("🌟 IMPROVED ULTIMATE 4-MODEL PROMPT ENGINEERING PLATFORM")
        print("=" * 75)
        print("Enhanced: OpenAI • Meta Llama • Google Gemini • Anthropic Claude")
        print("=" * 75)
        
        # Load API keys (including multiple Google keys)
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.llama_key = os.getenv('LLAMA_API_KEY')
        self.google_keys = [
            os.getenv('GOOGLE_API_KEY'),
            os.getenv('GOOGLE_API_KEY_BACKUP'), 
            os.getenv('GOOGLE_API_KEY_BACKUP2')
        ]
        self.google_keys = [k for k in self.google_keys if k]  # Remove None values
        self.claude_key = os.getenv('CLAUDE_API_KEY')
        
        # Track active keys and clients
        self.active_google_key = None
        self.active_google_model = None
        self.clients = {}
        
        # Display key status
        self.check_all_api_keys()
        
        # Initialize all clients
        self.setup_all_clients()
        
        # Display final status
        self.display_platform_status()
    
    def check_all_api_keys(self):
        """Check and display all API key statuses"""
        
        print("\n🔐 Enhanced API Key Status Check:")
        print("-" * 45)
        
        keys_status = {
            "OpenAI GPT": self.openai_key and self.openai_key != "your-openai-key-here",
            "Meta Llama": bool(self.llama_key),
            "Google Gemini": len(self.google_keys) > 0,
            "Anthropic Claude": bool(self.claude_key)
        }
        
        working_keys = 0
        for service, has_key in keys_status.items():
            status = "✅" if has_key else "❌"
            if service == "Google Gemini" and has_key:
                print(f"{status} {service} ({len(self.google_keys)} keys available)")
            else:
                print(f"{status} {service}")
            if has_key:
                working_keys += 1
        
        print(f"\n📊 {working_keys}/4 AI providers configured")
        
        if working_keys == 4:
            print("🎉 PERFECT! All 4 AI providers configured!")
        elif working_keys >= 3:
            print("🔥 EXCELLENT! Multiple AI providers configured!")
        elif working_keys >= 2:
            print("✅ GOOD! You have multiple models to compare!")
        else:
            print("⚠️  Limited functionality - add more API keys")
        
        return working_keys > 0
    
    def setup_openai_client(self):
        """Setup OpenAI client"""
        
        if not self.openai_key or self.openai_key == "your-openai-key-here":
            print("⚠️  OpenAI key not configured")
            return False
        
        try:
            from openai import OpenAI
            self.clients['openai'] = OpenAI(api_key=self.openai_key)
            print("✅ OpenAI client initialized")
            return True
        except Exception as e:
            print(f"❌ OpenAI setup failed: {str(e)[:75]}")
            return False
    
    def setup_claude_client(self):
        """Setup Claude (Anthropic) client with improved model handling"""
        
        if not self.claude_key:
            print("⚠️  Claude API key not configured")
            return False
        
        try:
            import anthropic
            self.clients['claude'] = anthropic.Anthropic(api_key=self.claude_key)
            print("✅ Claude client initialized")
            return True
        except Exception as e:
            print(f"❌ Claude setup failed: {str(e)[:75]}")
            return False
    
    def setup_google_client(self):
        """Setup Google client with multiple keys and model versions"""
        
        if not self.google_keys:
            print("⚠️  No Google keys available")
            return False
        
        # Import Google AI library
        try:
            import google.generativeai as genai
        except ImportError:
            print("❌ Google AI library not available")
            return False
        
        # Try different model names
        model_names_to_try = [
            'gemini-1.5-pro-latest',
            'gemini-1.5-pro', 
            'gemini-pro',
            'gemini-1.0-pro'
        ]
        
        # Try each key with each model name
        for key_idx, key in enumerate(self.google_keys):
            for model_name in model_names_to_try:
                try:
                    genai.configure(api_key=key)
                    model = genai.GenerativeModel(model_name)
                    
                    # Test with minimal request
                    test_response = model.generate_content(
                        "Hi", generation_config={'max_output_tokens': 5}
                    )
                    
                    # Success!
                    self.active_google_key = key
                    self.active_google_model = model_name
                    self.clients['google'] = model
                    key_name = f"Key #{key_idx+1}" if key_idx > 0 else "Primary"
                    print(f"✅ Google Gemini ready ({key_name} key, model: {model_name})")
                    return True
                    
                except Exception as e:
                    # Try next combination
                    continue
        
        print("❌ All Google key/model combinations failed")
        return False
    
    def setup_all_clients(self):
        """Setup all available API clients"""
        
        print("\n🔧 Initializing Enhanced AI Clients:")
        print("-" * 45)
        
        # Setup each service
        self.setup_openai_client()
        self.setup_claude_client()
        self.setup_google_client()
        
        # Llama uses HTTP requests, so just check key
        if self.llama_key:
            print("✅ Llama key configured (HTTP-based)")
        else:
            print("⚠️  Llama key not configured")
    
    def display_platform_status(self):
        """Display the final platform status"""
        
        available_models = []
        if 'openai' in self.clients:
            available_models.append("OpenAI GPT-4/3.5")
        if 'claude' in self.clients:
            available_models.append("Claude Sonnet")
        if 'google' in self.clients:
            available_models.append(f"Google Gemini ({self.active_google_model})")
        if self.llama_key:
            available_models.append("Meta Llama")
        
        print(f"\n🚀 ENHANCED PLATFORM READY!")
        print(f"Available Models: {len(available_models)}/4")
        for model in available_models:
            print(f"   🤖 {model}")
        
        if len(available_models) >= 3:
            print("\n🎉 ENHANCED ULTIMATE SETUP COMPLETE!")
            print("You have access to the best AI models for prompt engineering!")
        elif len(available_models) >= 2:
            print(f"\n✅ GREAT ENHANCED SETUP!")
            print("You can run comprehensive model comparisons!")
        elif len(available_models) >= 1:
            print(f"\n✅ BASIC ENHANCED SETUP READY!")
            print("You can start prompt engineering experiments!")
        else:
            print(f"\n⚠️  No models available. Please check your API keys.")
    
    # Model-specific response methods with improved error handling
    def get_openai_response(self, prompt: str, system_prompt: Optional[str] = None, model: str = "gpt-4") -> str:
        """Get response from OpenAI"""
        
        if 'openai' not in self.clients:
            return "❌ OpenAI not available"
        
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            response = self.clients['openai'].chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=400,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ OpenAI Error: {str(e)[:100]}"
    
    def get_claude_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Get response from Claude with updated model"""
        
        if 'claude' not in self.clients:
            return "❌ Claude not available"
        
        try:
            # Use the latest stable Claude model
            messages = [{"role": "user", "content": prompt}]
            
            kwargs = {
                "model": "claude-3-5-sonnet-20241022",  # Updated model
                "max_tokens": 400,
                "temperature": 0.7,
                "messages": messages
            }
            
            if system_prompt:
                kwargs["system"] = system_prompt
            
            response = self.clients['claude'].messages.create(**kwargs)
            return response.content[0].text
            
        except Exception as e:
            error_msg = str(e)
            if "overloaded" in error_msg.lower():
                return "❌ Claude temporarily overloaded - try again in a moment"
            else:
                return f"❌ Claude Error: {error_msg[:100]}"
    
    def get_llama_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Get response from Llama with improved error handling"""
        
        if not self.llama_key:
            return "❌ Llama not available"
        
        try:
            url = "https://api.llama.com/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.llama_key}"
            }
            
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            data = {
                "model": "Llama-4-Maverick-17B-128E-Instruct-FP8",
                "messages": messages,
                "max_tokens": 400,
                "temperature": 0.7
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                # Improved parsing to handle different response formats
                if 'choices' in result and len(result['choices']) > 0:
                    if 'message' in result['choices'][0]:
                        return result['choices'][0]['message']['content']
                    elif 'text' in result['choices'][0]:
                        return result['choices'][0]['text']
                return "❌ Unexpected Llama response format"
            else:
                return f"❌ Llama API Error: {response.status_code}"
                
        except Exception as e:
            return f"❌ Llama Error: {str(e)[:100]}"
    
    def get_google_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Get response from Google Gemini"""
        
        if 'google' not in self.clients:
            return "❌ Google not available"
        
        try:
            # Combine system and user prompt for Gemini
            full_prompt = prompt
            if system_prompt:
                full_prompt = f"Instructions: {system_prompt}\n\nUser: {prompt}"
            
            response = self.clients['google'].generate_content(
                full_prompt,
                generation_config={
                    'max_output_tokens': 400,
                    'temperature': 0.7
                }
            )
            return response.text
        except Exception as e:
            return f"❌ Google Error: {str(e)[:100]}"
    
    def run_enhanced_4model_test(self):
        """Test all 4 AI model connections with enhanced error handling"""
        
        print("\n🧪 ENHANCED 4-MODEL CONNECTION TEST")
        print("=" * 55)
        
        test_prompt = "Hello! Respond with just 'Connection successful!' to test."
        
        models = {
            "OpenAI GPT-4": lambda: self.get_openai_response(test_prompt),
            "Claude Sonnet": lambda: self.get_claude_response(test_prompt),
            "Google Gemini": lambda: self.get_google_response(test_prompt),
            "Meta Llama": lambda: self.get_llama_response(test_prompt)
        }
        
        working_models = []
        
        for model_name, test_func in models.items():
            print(f"\n🔄 Testing {model_name}...")
            
            result = test_func()
            
            if not result.startswith("❌"):
                print(f"✅ {model_name}: SUCCESS")
                print(f"   Response: {result[:60]}...")
                working_models.append(model_name)
            else:
                print(f"❌ {model_name}: FAILED")
                print(f"   Error: {result[:80]}")
        
        # Enhanced summary
        print(f"\n📊 ENHANCED CONNECTION TEST RESULTS:")
        print(f"✅ Working models: {len(working_models)}/4")
        
        if len(working_models) == 4:
            print("🎉 PERFECT! All 4 AI providers are working!")
            print("You have the ultimate prompt engineering setup!")
        elif len(working_models) >= 3:
            print(f"🔥 EXCELLENT! {len(working_models)} models working!")
            print("You can run comprehensive model comparisons!")
        elif len(working_models) >= 2:
            print(f"✅ GOOD! {len(working_models)} models working!")
            print("You can run effective model comparisons!")
        elif len(working_models) == 1:
            print("✅ BASIC! 1 model working - you can start experimenting!")
        else:
            print("⚠️  No models working. Please check your API keys.")
        
        return working_models
    
    def compare_all_models_enhanced(self, prompt: str, system_prompt: Optional[str] = None, title: str = "🌟 Enhanced 4-Model Comparison"):
        """Enhanced comparison across all 4 AI models"""
        
        print(f"\n{title}")
        print(f"Prompt: {prompt}")
        if system_prompt:
            print(f"System: {system_prompt}")
        print("=" * 80)
        
        models = {
            "🧠 OpenAI GPT-4": lambda: self.get_openai_response(prompt, system_prompt),
            "🎭 Claude Sonnet": lambda: self.get_claude_response(prompt, system_prompt),
            "🔍 Google Gemini": lambda: self.get_google_response(prompt, system_prompt),
            "🦙 Meta Llama": lambda: self.get_llama_response(prompt, system_prompt)
        }
        
        results = {}
        
        for model_name, model_func in models.items():
            print(f"\n{model_name}:")
            print("-" * 55)
            
            response = model_func()
            print(response)
            results[model_name] = response
            print()
        
        return results
    
    def interactive_mode_enhanced(self):
        """Enhanced interactive prompt testing across 4 models"""
        
        print("\n🎮 ENHANCED INTERACTIVE MODE")
        print("=" * 55)
        print("🌟 Test prompts across OpenAI, Claude, Gemini, and Llama!")
        print()
        print("Commands:")
        print("  • Enter any prompt to test across all available models")
        print("  • Type 'test' to rerun connection tests")
        print("  • Type 'quit' to exit")
        print("-" * 55)
        
        while True:
            print(f"\n💭 Your prompt (or command): ")
            user_input = input().strip()
            
            if not user_input:
                continue
            elif user_input.lower() == 'quit':
                print("👋 Thanks for using the Enhanced Ultimate 4-Model Platform!")
                print("🎓 You're now ready for advanced prompt engineering!")
                break
            elif user_input.lower() == 'test':
                self.run_enhanced_4model_test()
                continue
            
            # Get optional system prompt
            print("🔧 System prompt (optional, press Enter to skip): ")
            system_input = input().strip()
            system_prompt = system_input if system_input else None
            
            # Run enhanced 4-model comparison
            self.compare_all_models_enhanced(user_input, system_prompt, "🎯 Your Enhanced Custom Test")


def main():
    """Main function to run the enhanced ultimate 4-model platform"""
    
    try:
        # Initialize the enhanced platform
        platform = ImprovedUltimate4ModelPlatform()
        
        # Run enhanced connection tests
        working_models = platform.run_enhanced_4model_test()
        
        if len(working_models) > 0:
            print(f"\n🎓 ENHANCED ULTIMATE PLATFORM READY!")
            print("You now have the most comprehensive prompt engineering setup possible!")
            
            # Enhanced menu options
            print(f"\n🚀 What would you like to do?")
            print("1. 🎮 Start enhanced interactive 4-model testing mode")
            print("2. 🎯 Quick enhanced single prompt test")
            print("3. 📚 Exit (use this in Jupyter notebooks)")
            
            while True:
                choice = input(f"\nEnter your choice (1-3): ").strip()
                
                if choice == "1":
                    platform.interactive_mode_enhanced()
                    break
                elif choice == "2":
                    prompt = input("Enter your test prompt: ")
                    platform.compare_all_models_enhanced(prompt, title="Quick Enhanced 4-Model Test")
                    break
                elif choice == "3":
                    print(f"\n✅ Enhanced ultimate platform ready for import!")
                    print("In Jupyter: from improved_ultimate_4model_setup import ImprovedUltimate4ModelPlatform")
                    print("           platform = ImprovedUltimate4ModelPlatform()")
                    break
                else:
                    print("Please enter 1, 2, or 3")
        
        else:
            print(f"\n⚠️  No models are working. Please:")
            print("1. Check your .env file exists and has correct API keys")
            print("2. Ensure billing is enabled on your accounts") 
            print("3. Check your internet connection")
            print("4. Verify API key permissions")
    
    except KeyboardInterrupt:
        print(f"\n\n👋 Setup interrupted. Run again when ready!")
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        print("Please check your .env file, API keys, and internet connection.")


if __name__ == "__main__":
    main()
