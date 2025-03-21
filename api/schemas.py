from pydantic import BaseModel
from typing import List, Optional

class MedicationInput(BaseModel):
    medication1: str
    medication2: str

class MedicationInfo(BaseModel):
    medicationName: str
    thereIsConflict: bool

class InteractionResponse(BaseModel):
    medications: List[MedicationInfo]
    description: str
    alternatives: List[str]