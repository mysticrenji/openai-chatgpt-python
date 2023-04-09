import os
import openai
import sys

api_key = os.getenv('API_KEY')
gpt_model = os.getenv('MODEL')
role = os.getenv('ROLE')
if api_key is None or api_key == "":
    print("API_KEY is empty. Please provide an API_KEY from OpenAI Service")
    exit(0)

if gpt_model is None or gpt_model == "":
    gpt_model = 'gpt-3.5-turbo'
else:
    print("Taking model: ", gpt_model)

openai.api_key = api_key
if role is None or role == "":
    role = "user"
else:
    print("Taking role: ", role)

if len(sys.argv) != 2:
    print("Usage: python script_name.py 'your message'")
else:
    message = sys.argv[1]
    print("You asked -",message)

result = openai.ChatCompletion.create(
    model=gpt_model,
    messages=[{"role": role,
               "content": message}]
)

print(result.choices[0].message.content)

