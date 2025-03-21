from fastapi import APIRouter, HTTPException
from src.core.openai_client import get_completion, clean_prompt
from src.api.schemas import MedicationInput, InteractionResponse
import json

router = APIRouter()

@router.post("/check-interaction", response_model=InteractionResponse)
async def check_interaction(data: MedicationInput):
    prompt = f"""
    Gere apenas um JSON em formato de texto, sem marcação de código. A resposta deve começar diretamente com '{{'. 

    O JSON deve conter informações sobre interações medicamentosas entre os fármacos: {data.medication1} e {data.medication2}.

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
      "description": "Resumo sucinto e com poucos caracteres do motivo da interação, seguindo o padrão de bulas.",
      "alternatives": [
        "Medicamento alternativo 1 que pode ser ministrado com o 2, especifique apenas a medicação",
        "Medicamento alternativo 2 que pode ser ministrado com o 1, especifique apenas a medicação"
      ]
    }}
    """
    try:
        response = clean_prompt(get_completion(prompt))
        return json.loads(response)  # Converte a resposta para JSON
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))