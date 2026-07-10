from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

# read key
api_key = os.getenv("ANTHROPIC_API_KEY")


# check if it is loaded
if api_key:
    print("✅ Key is loaded successfully!")
    print("Key starts with:", api_key[:6])  # show only partial for safety
else:
    print("❌ Key NOT found. Check your .env file.")