# Makers Tech Test - Bank

This is an excercise to demostrate design process and TDD appraoch with a simple bank account app.

## Technology Decisions

* **Language**: Python
* **IDE**: VSCode
* **Testsuite**: unittest
* **Coding Style Guide:** Python PEP-8

## Assumptions

* No error checking on format of input data format to be performed
* No negative balance check to be implemented
* Output will be in the format shown in specification (below)

```
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```

* Output will be a return from a function rather than printed to STDIO

## System Design

* Class to be created with balance varaible tracking the account balance and transactions list that will keep a record of all the transactions that occur on the account.
* Interaction to the account will be through`deposit` and`withdraw` functions that will take the input of the account, amount and transaction date.
* Statement for the transactions on the account can be viewed with`display_balance` function, the output format is shown in the assumptions.

## Test Plan

This is the test steps that will be used to build up the functionality through TDD and the Red-Green-Refactor loop process.

1. Create instance of BankAccount class
2. Create instance of BankAccount class and check balance is zero
3. Create instance of BankAccount class with custom starting balance
4. Deposit - Increment balance by set amount
5. Withdraw - Decement balance by set amount
6. Display - Statement can be viewed in correct format with dummy data
7. Display - Statement can be viewed in correct format with real deposit amount and todays date
8. Display - Statement can be viewed in correct format with real withdraw amount and todays date
9. Deposit - Default transaction date is today
10. Withdraw - Default transaction date is today
11. Display - Statement can be viewed in correct format and order with real incomplete data (with todays date)
12. Deposit - Transaction date can be set in call to deposit
13. WIthdraw - Transaction date can be set in call to withdraw
14. Display - Statement can be viewed in correct format with real complete data (with customised date) (CUSTOMER ACCEPTANCE TEST)

## Testing the Application

Instructions to exectute the test suite on the application.

###Pre-Requisites

* Python 3.x or later installed (this can checked by running:`python --version`, output should be something like this:`Python 3.8.5`
* Unittest framework is included as a standar library in Python 3.x and later.

### Test Instructions

* Download the application to your local directory.
* Navigate to the directory when the app is located.
* Execute the following command:`python bankaccounttests.py`

### Test Results

The following results should be displayed for a test pass:

Note: There is a skipped test but kept in the code to show test progression through development.

```
.....x........
----------------------------------------------------------------------
Ran 14 tests in 0.008s
OK (expected failures=1)
```

## Usage Instruction

The following are the instructions to use the application.

* Load the Python REPL and import the `bankaccount.py` file.

`python -i bankaccount.py`

* Create a new account called account and specify the starting balance (leave blank for 0).

`account = BankAccount(50)`

* User can deposit and withdraw using the following commands, specify an amount and a transaction date (the date will be today if left blank)

`account.deposit(100, "10/08/2020")`

`account.withdraw(50)`

* User can view the human-readable statement using the following command. Note that the `display_statement()` is wrapped in the `print` statement, this is to ensure the formatting is displayed correctly as the application returns the data in a `return` rather than printed to the std output.~~~~

`print(account.display_statement())`
