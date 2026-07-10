# Install dependencies: pip install anthropic python-dotenv
#Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Create an API Client
from anthropic import Anthropic

client =Anthropic()
model = "claude-sonnet-5"

#make a request
message=client.messages.create(
    model=model,
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
print(message.content[0].text)