##The Anthropic API and Claude do not store any messages.(because the Anthropic Messages API is stateless)
##To have a 'conversation', you need to:
##1. Manually maintain a list of messages in your code
##2. Provide that list of messages with each follow up request to the model.

#loading environment variables from .env file
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()

#Create an API Client
client =Anthropic()
model="claude-sonnet-5"


def add_user_message(messages, text):
    user_message={"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message={"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message=client.messages.create(
        model=model,
        max_tokens=100,
        messages=messages
    )
    return message.content

#Make a starting list of messages
messages=[]

#Add in the initial user question of "What is quantum computing? Answer in one sentence"
add_user_message(messages, "What is quantum computing? Answer in one sentence")

# Pass the list of messages into 'chat' (to the model) and get a response
answer=chat(messages)

#Take the answer and add it as an assistant message to the list of messages
add_assistant_message(messages, answer)

#Add in the users follow-up question
add_user_message(messages, "write another sentence")

#Call chat again with the list of messages to get a final answer
answer=chat(messages)

print(answer)