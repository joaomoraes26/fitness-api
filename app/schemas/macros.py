from pydantic import BaseModel

class MacrosEstimados(BaseModel):
    calorias : float
    proteina : float
    carboidrato : float
    gordura : float 