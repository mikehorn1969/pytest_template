import pytest 
from pytest_bdd import scenarios, scenario, given, when, then, parsers
  
# Load all scenarios from the feature file  
scenarios("../features/bank_transactions.feature")  
  
# Fixtures  
@pytest.fixture  
def account_balance():  
    return {"balance": 0}  # Using a dictionary to allow modifications  
  
# Given Steps  
@given(parsers.parse('the account balance is £"{balance:d}"'), target_fixture="account_balance",)
def account_initial_balance(account_balance, balance):  
    account_balance["balance"] = balance  
  
# When Steps  
@when(parsers.parse('I deposit £"{deposit:d}"')) 
def deposit(account_balance, deposit):  
    account_balance["balance"] += deposit  
  
# When Steps  
@when(parsers.parse('I withdraw £"{withdrawal:d}"')) 
def deposit(account_balance, withdrawal):  
    account_balance["balance"] -= withdrawal  

  
# Then Steps  
@then(parsers.parse('the account balance should be £"{new_balance:d}"'))
def account_balance_should_be(account_balance, new_balance):  
    assert account_balance["balance"] == new_balance
