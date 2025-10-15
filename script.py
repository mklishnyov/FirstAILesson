import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Объясни, что такое токен в LLM"}
    ]
}

response = requests.post(url, headers = headers, json = data)

result = response.json()

print(result["choices"][0]["message"]["content"])