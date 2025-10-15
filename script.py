import requests
import json
import os

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
}
data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Объясни, что такое токен в LLM"}]
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
