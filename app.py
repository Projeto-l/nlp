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

prompt = f"""
Gere uma lista com as contraindicações de um medicamento específico,\
citando medicações que não podem ser ministradas em conjunto \
organize em tópicos numerados. Por exemplo: \
1. Dipirona \
2. Rivotril \

Se possível, forneça uma fonte confiável (sem link para páginas). Inclua também \
situações em que o medicamento não deve ser administrado, como o caso de uma gestante \ 
que não pode usar Roacutan. \

Não é necessário explicar suas decisões; retorne apenas a lista com as contraindicações \
e a fonte, sem muitos detalhes ou observações adicionais. \
Evite usar formatação em negrito nas palavras (por exemplo: **palavra**). \

medicamento exemplo: amoxicilina \
"""

response = get_completion(prompt)
print(response)