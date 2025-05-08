# main.py
from agents import IdentityDocumentAgent, IncomeReceiptAgent, ContractAgent
from validators import IdentityValidator, IncomeValidator, ContractValidator
from report import ReportGenerator

identity_agent = IdentityDocumentAgent()
income_agent = IncomeReceiptAgent()
contract_agent = ContractAgent()

identity_validator = IdentityValidator()
income_validator = IncomeValidator()
contract_validator = ContractValidator()

report_generator = ReportGenerator()

# Extract data
tenants = identity_agent.extract(list_file_ci[0][1])
incomes = income_agent.extract(list_file_recipients[0][1])
contract = contract_agent.extract(file_contract[0])

# Validate data
identity_validation = identity_validator.validate(tenants)
income_validation = income_validator.validate(incomes)
contract_validation = contract_validator.validate(contract)

# Generate report
report = report_generator.generate(contract, [identity_validation, income_validation, contract_validation])