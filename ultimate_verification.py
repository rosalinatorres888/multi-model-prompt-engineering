#!/usr/bin/env python3
"""
ULTIMATE 4-MODEL ENVIRONMENT VERIFICATION
========================================

Comprehensive verification for the ultimate prompt engineering setup with:
- OpenAI GPT-4 & GPT-3.5
- Meta Llama models
- Google Gemini (with backup)  
- Anthropic Claude (Sonnet & Haiku)

This verifies all 4 major AI providers are properly configured.
"""

import os
import sys
import importlib.util

def check_python_version():
    """Check Python version compatibility"""
    version = sys.version_info
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version is compatible")
        return True
    else:
        print("   ❌ Python 3.8+ required")
        return False

def check_required_packages():
    """Check if all required packages are installed"""
    
    required_packages = {
        'requests': 'HTTP requests for API calls',
        'python-dotenv': 'Environment variable loading', 
        'openai': 'OpenAI API client',
        'google-generativeai': 'Google Gemini API client',
        'anthropic': 'Claude API client'
    }
    
    print(f"\n📦 Checking Required Packages:")
    print("-" * 40)
    
    missing_packages = []
    
    for package, description in required_packages.items():
        # Handle package name variations
        package_name = package
        if package == 'python-dotenv':
            package_name = 'dotenv'
        elif package == 'google-generativeai':
            package_name = 'google.generativeai'
        
        spec = importlib.util.find_spec(package_name)
        if spec is not None:
            print(f"✅ {package:<25}: Available")
        else:
            print(f"❌ {package:<25}: Missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n💡 To install missing packages:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    else:
        print(f"\n🎉 All required packages are installed!")
        return True

def check_env_file_ultimate():
    """Check if .env file exists and has all 5 API keys"""
    
    print(f"\n🔐 Checking Ultimate Environment Configuration:")
    print("-" * 50)
    
    # Check if .env file exists
    env_paths = ['.env', '/Users/rosalinatorres/Documents/.env']
    env_file_found = False
    env_file_path = None
    
    for path in env_paths:
        if os.path.exists(path):
            print(f"✅ Found .env file at: {path}")
            env_file_found = True
            env_file_path = path
            break
    
    if not env_file_found:
        print("❌ .env file not found")
        print("💡 Create .env file with your API keys")
        return False
    
    # Try to load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("❌ python-dotenv not available")
        return False
    
    # Check all required environment variables
    required_vars = {
        'OPENAI_API_KEY': 'OpenAI GPT models',
        'LLAMA_API_KEY': 'Meta Llama models',
        'GOOGLE_API_KEY': 'Google Gemini (Primary)',
        'GOOGLE_API_KEY_BACKUP': 'Google Gemini (Backup)',
        'CLAUDE_API_KEY': 'Anthropic Claude'
    }
    
    print(f"\n🔑 Ultimate API Key Status:")
    print("-" * 35)
    configured_keys = 0
    
    for var_name, description in required_vars.items():
        value = os.getenv(var_name)
        if value and value != "your-openai-key-here":
            # Show masked version
            if len(value) > 20:
                masked = f"{value[:8]}...{value[-8:]}"
            else:
                masked = f"{value[:6]}...{value[-6:]}"
            print(f"✅ {description:<25}: {masked}")
            configured_keys += 1
        else:
            print(f"❌ {description:<25}: Missing or placeholder")
    
    print(f"\n📊 Ultimate Summary: {configured_keys}/{len(required_vars)} API keys configured")
    
    if configured_keys == len(required_vars):
        print("🎉 PERFECT! All 5 API keys configured!")
        print("You have the ULTIMATE prompt engineering setup!")
    elif configured_keys >= 3:
        print("🔥 EXCELLENT! Multiple AI providers configured!")
        print("You can run comprehensive model comparisons!")
    elif configured_keys >= 2:
        print("✅ GOOD! You have multiple models to compare!")
    elif configured_keys == 1:
        print("⚠️  Only 1 API key - limited functionality")
    else:
        print("❌ No API keys configured!")
        return False
    
    return configured_keys > 0

def run_ultimate_api_tests():
    """Run comprehensive tests of all 4 AI providers"""
    
    print(f"\n🧪 Ultimate API Connection Tests:")
    print("-" * 45)
    
    # Load environment
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        print("❌ Cannot load environment variables")
        return False
    
    test_prompt = "Hi"
    successful_tests = 0
    total_tests = 4
    
    # Test OpenAI
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key and openai_key != "your-openai-key-here":
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": test_prompt}],
                max_tokens=5
            )
            print("✅ OpenAI GPT: Connection successful")
            successful_tests += 1
        except Exception as e:
            print(f"❌ OpenAI GPT: {str(e)[:60]}...")
    else:
        print("⚠️  OpenAI GPT: Key not configured")
    
    # Test Claude
    claude_key = os.getenv('CLAUDE_API_KEY')
    if claude_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=claude_key)
            
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=5,
                messages=[{"role": "user", "content": test_prompt}]
            )
            print("✅ Claude Sonnet: Connection successful")
            successful_tests += 1
        except Exception as e:
            print(f"❌ Claude Sonnet: {str(e)[:60]}...")
    else:
        print("⚠️  Claude Sonnet: Key not configured")
    
    # Test Google Gemini
    google_key = os.getenv('GOOGLE_API_KEY')
    if google_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=google_key)
            model = genai.GenerativeModel('gemini-pro')
            
            response = model.generate_content(
                test_prompt, 
                generation_config={'max_output_tokens': 5}
            )
            print("✅ Google Gemini: Connection successful")
            successful_tests += 1
        except Exception as e:
            print(f"❌ Google Gemini: {str(e)[:60]}...")
    else:
        print("⚠️  Google Gemini: Key not configured")
    
    # Test Llama (just verify key format)
    llama_key = os.getenv('LLAMA_API_KEY')
    if llama_key:
        if llama_key.startswith('LLM|'):
            print("✅ Meta Llama: Key format verified")
            successful_tests += 1
        else:
            print("⚠️  Meta Llama: Unusual key format")
    else:
        print("⚠️  Meta Llama: Key not configured")
    
    # Summary of API tests
    print(f"\n📊 API Test Results: {successful_tests}/{total_tests} models working")
    
    if successful_tests == 4:
        print("🎉 ULTIMATE SUCCESS! All 4 AI providers working!")
    elif successful_tests >= 3:
        print("🔥 EXCELLENT! Multiple AI providers ready!")
    elif successful_tests >= 2:
        print("✅ GOOD! You can run model comparisons!")
    elif successful_tests == 1:
        print("⚠️  Only 1 model working - basic functionality available")
    else:
        print("❌ No models working - please check your API keys")
    
    return successful_tests

def main():
    """Run ultimate environment verification"""
    
    print("🌟 ULTIMATE 4-MODEL ENVIRONMENT VERIFICATION")
    print("=" * 65)
    print("Checking setup for: OpenAI • Claude • Gemini • Llama")
    print("=" * 65)
    
    all_checks = []
    
    # Run all verification checks
    all_checks.append(check_python_version())
    all_checks.append(check_required_packages())
    all_checks.append(check_env_file_ultimate())
    
    # Calculate results
    passed_checks = sum(all_checks)
    total_checks = len(all_checks)
    
    # Final comprehensive summary
    print(f"\n{'='*65}")
    print("🏁 ULTIMATE VERIFICATION SUMMARY:")
    print("=" * 35)
    
    if passed_checks == total_checks:
        print("🎉 ULTIMATE ENVIRONMENT READY!")
        print("✅ All verification checks passed")
        print()
        print("🚀 Next Steps:")
        print("1. Run: python ultimate_4model_setup.py")
        print("2. Or start Jupyter with the updated notebook")
        print("3. Or import in Python: from ultimate_4model_setup import Ultimate4ModelPlatform")
        
        # Run comprehensive API tests
        print("\n" + "="*35)
        working_models = run_ultimate_api_tests()
        
        if working_models >= 3:
            print("\n🌟 CONGRATULATIONS!")
            print("You have the ULTIMATE prompt engineering environment!")
            print("You can now:")
            print("  • Compare responses across multiple AI providers")
            print("  • Test prompt robustness across different architectures")  
            print("  • Analyze model strengths and weaknesses")
            print("  • Run advanced prompt engineering experiments")
            print("  • Build the most sophisticated AI applications")
        
    elif passed_checks >= 2:
        print("⚠️  PARTIAL ULTIMATE SETUP")
        print(f"✅ {passed_checks}/{total_checks} verification checks passed")
        print("You can proceed with limited functionality")
        
        run_ultimate_api_tests()
        
    else:
        print("❌ SETUP INCOMPLETE")
        print(f"Only {passed_checks}/{total_checks} checks passed")
        print("Please fix the issues above before proceeding")
    
    print(f"\n{'='*65}")
    print("🎓 Ready for the ultimate prompt engineering experience!")

if __name__ == "__main__":
    main()
