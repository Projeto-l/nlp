from dotenv import load_dotenv
from openai import OpenAI
import os
import re

load_dotenv()

client = OpenAI(
	base_url="https://openrouter.ai/api/v1",
	api_key= os.getenv("TOKEN")
)

def get_completion(prompt, model="google/gemini-2.0-pro-exp-02-05:free"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=500
    )
    return response.choices[0].message.content

def clean_prompt(prompt):
    return re.sub(r"^```json\n|```$", "", prompt.strip(), flags=re.MULTILINE)