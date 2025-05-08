# validators.py
from models import Tenant, Contract

class IdentityValidator:
    def validate(self, tenant: Tenant):
        # Validate tenant's identity
        pass

class IncomeValidator:
    def validate(self, tenant: Tenant):
        # Validate tenant's income
        pass

class ContractValidator:
    def validate(self, contract: Contract):
        # Validate contract
        pass