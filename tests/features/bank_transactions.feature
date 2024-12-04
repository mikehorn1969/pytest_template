Feature: Bank Transactions

    Tests related to banking Transactions

   """  Scenario: Deposit into account
        Given the account balance is £"100"
        When I deposit £"20"
        Then the account balance should be £"120"

    Scenario: Withdraw from account
        Given the account balance is £"100"
        When I withdraw £"20"
        Then the account balance should be £"80" """
        
    Scenario Outline: Deposit into account
        Given the account balance - £<balance>
        When I deposit £<deposit>
        Then the account balance should be £<new_balance>
        Examples:
            | balance | deposit | new_balance |
            | 100     | 20      | 120         |
            | 0       | 5       | 5           |
            | 100     | 0       | 100         |

    Scenario Outline:  Withdraw from account
        Given the account balance is £<balance>
        When I withdraw £<withdrawal>
        Then the account balance should be £<new_balance>
        Examples
            | balance | withdrawal | new_balance |
            | 100     | 20         | 80          |
            | 0       | 5          | -5          |
            | 100     | 0          | 100         |

