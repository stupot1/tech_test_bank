# Makers Tech Test - Bank

This is an excercise to demostrate design process and TDD appraoch with a simple bank account app.

## Technology Decisions

* **Language**: Python
* **IDE**: VSCode
* **Testsuite**: unittest

## Test Plan

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
11. Display - Statement can be viewed in correct format and order ~~~~with real incomplete data (with todays date)
12. Deposit - Transaction date can be set in call to deposit
13. WIthdraw - Transaction date can be set in call to withdraw
14. Display - Statement can be viewed in correct format with real complete data (with customised date) (CUSTOMER ACCEPTANCE TEST)
