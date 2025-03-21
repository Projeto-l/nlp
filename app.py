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

medication = f"""
SImvastatina e Atorvastatina
"""

prompt = f"""
Gere apenas um JSON em formato de texto, sem marcação de código. A resposta deve começar diretamente com '{{'. 

O JSON deve conter informações sobre interações medicamentosas entre os fármacos: {medication}.

O JSON deve seguir esta estrutura exata:

{{
  "medications": [
    {{
      "medicationName": "Nome comum do medicamento 1",
      "thereIsConflict": "True ou False"
    }},
    {{
      "medicationName": "Nome comum do medicamento 2",
      "thereIsConflict": "True ou False"
    }}
  ],
  "description": "Resumo sucinto e com poucos caracteres do motivo da interação, seguindo o padrão de bulas. 
   Exemplo: 'Microdoses de progesterona são inadequadas durante o tratamento com isotretinoína, devido a ...'",
  "alternatives": [
    "Medicamento alternativo 1 que pode ser ministrado com o 2, especifique apenas a medicação",
    "Medicamento alternativo 2 que pode ser ministrado com o 1, especifique apenas a medicação"
  ]
  observação: Caso thereIsConflict seja "Não", alternatives será no formato: "alternatives": []
}}
"""

response = clean_prompt(get_completion(prompt))
print(response)