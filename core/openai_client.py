from dotenv import load_dotenv
from openai import OpenAI
import os
import re

load_dotenv()

client = OpenAI(
	base_url="https://openrouter.ai/api/v1",
	api_key= os.getenv("TOKEN")
)

def get_completion(prompt: str, model: str = "anthropic/claude-3-haiku:free") -> str:
    try:
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=800
        )
        print("Resposta bruta da API:", response)  # Debug
        return response.choices[0].message.content
    except Exception as e:
        print("Erro na chamada da API:", str(e))  # Debug
        return None

def clean_prompt(prompt):
    return re.sub(r"^```json\n|```$", "", prompt.strip(), flags=re.MULTILINE)