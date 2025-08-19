#!/usr/bin/env python3
"""
ENVIRONMENT VERIFICATION SCRIPT
==============================

This script checks if your prompt engineering environment is properly configured.
Run this first to verify your setup before starting your experiments.
"""

import os
import sys
import importlib.util

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version is compatible")
        return True
    else:
        print("   ❌ Python 3.8+ required")
        return False

def check_required_packages():
    """Check if required packages are installed"""
    
    required_packages = {
        'requests': 'HTTP requests for API calls',
        'python-dotenv': 'Environment variable loading', 
        'openai': 'OpenAI API client',
        'google-generativeai': 'Google Gemini API client'
    }
    
    print(f"\n📦 Checking Required Packages:")
    print("-" * 35)
    
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
            print(f"✅ {package:<20}: Available")
        else:
            print(f"❌ {package:<20}: Missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n💡 To install missing packages:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    else:
        print(f"\n✅ All required packages are installed!")
        return True

def check_env_file():
    """Check if .env file exists and has required keys"""
    
    print(f"\n🔐 Checking Environment Configuration:")
    print("-" * 40)
    
    # Check if .env file exists
    env_paths = ['.env', '/Users/rosalinatorres/Documents/.env']
    env_file_found = False
    
    for path in env_paths:
        if os.path.exists(path):
            print(f"✅ Found .env file at: {path}")
            env_file_found = True
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
    
    # Check required environment variables
    required_vars = {
        'OPENAI_API_KEY': 'OpenAI API access',
        'LLAMA_API_KEY': 'Llama model access',
        'GOOGLE_API_KEY': 'Google Gemini access',
        'GOOGLE_API_KEY_BACKUP': 'Google Gemini backup'
    }
    
    print(f"\n🔑 API Key Status:")
    configured_keys = 0
    
    for var_name, description in required_vars.items():
        value = os.getenv(var_name)
        if value and value != "your-openai-key-here":
            print(f"✅ {var_name:<25}: Configured")
            configured_keys += 1
        else:
            print(f"❌ {var_name:<25}: Missing or placeholder")
    
    print(f"\n📊 Summary: {configured_keys}/{len(required_vars)} API keys configured")
    
    if configured_keys == 0:
        print("⚠️  No API keys configured!")
        return False
    elif configured_keys < len(required_vars):
        print("⚠️  Some API keys missing - limited functionality")
        return True
    else:
        print("🎉 All API keys configured!")
        return True

def run_quick_api_test():
    """Run a quick test of available APIs"""
    
    print(f"\n🧪 Quick API Connection Test:")
    print("-" * 35)
    
    # Load environment
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        print("❌ Cannot load environment variables")
        return False
    
    # Test OpenAI
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key and openai_key != "your-openai-key-here":
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            
            # Very simple test
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hi"}],
                max_tokens=5
            )
            print("✅ OpenAI: Connection successful")
        except Exception as e:
            print(f"❌ OpenAI: {str(e)[:50]}...")
    else:
        print("⚠️  OpenAI: Key not configured")
    
    # Test Google
    google_key = os.getenv('GOOGLE_API_KEY')
    if google_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=google_key)
            model = genai.GenerativeModel('gemini-pro')
            
            response = model.generate_content(
                "Hi", 
                generation_config={'max_output_tokens': 5}
            )
            print("✅ Google Gemini: Connection successful")
        except Exception as e:
            print(f"❌ Google Gemini: {str(e)[:50]}...")
    else:
        print("⚠️  Google Gemini: Key not configured")
    
    # Test Llama (just check key format)
    llama_key = os.getenv('LLAMA_API_KEY')
    if llama_key:
        if llama_key.startswith('LLM|'):
            print("✅ Llama: Key format looks correct")
        else:
            print("⚠️  Llama: Unusual key format")
    else:
        print("⚠️  Llama: Key not configured")

def main():
    """Run complete environment verification"""
    
    print("🔍 PROMPT ENGINEERING ENVIRONMENT VERIFICATION")
    print("=" * 55)
    print("This script will check if your setup is ready for prompt engineering.")
    print()
    
    all_checks = []
    
    # Run all checks
    all_checks.append(check_python_version())
    all_checks.append(check_required_packages())
    all_checks.append(check_env_file())
    
    # Final summary
    print(f"\n{'='*55}")
    print("🏁 VERIFICATION SUMMARY:")
    
    passed = sum(all_checks)
    total = len(all_checks)
    
    if passed == total:
        print("🎉 ENVIRONMENT READY FOR PROMPT ENGINEERING!")
        print("✅ All checks passed")
        print()
        print("Next steps:")
        print("1. Run: python multi_model_setup.py")
        print("2. Or start Jupyter and import the setup")
        
        # Run API tests
        run_quick_api_test()
        
    elif passed >= 2:
        print("⚠️  PARTIAL SETUP DETECTED")
        print(f"✅ {passed}/{total} checks passed")
        print("You can proceed with limited functionality")
        
        run_quick_api_test()
        
    else:
        print("❌ SETUP INCOMPLETE")
        print(f"Only {passed}/{total} checks passed")
        print("Please fix the issues above before proceeding")
    
    print(f"\n{'='*55}")

if __name__ == "__main__":
    main()
