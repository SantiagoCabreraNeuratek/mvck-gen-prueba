# models.py
from pydantic import BaseModel

class Tenant(BaseModel):
    name: str
    ci: str
    income: float

class Contract(BaseModel):
    tenants: List[Tenant]
    rent: float