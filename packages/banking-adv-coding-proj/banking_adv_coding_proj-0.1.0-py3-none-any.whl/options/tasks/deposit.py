import sqlite3
from options.tasks.account_action import AccountAction

# child class: Deposit inherits from the parent class: AccountAction
class Deposit(AccountAction):
    def __init__(self, account_no, amount):
        # initializing the parent class with account number
        super().__init__(account_no)
        self.amount = amount

    def execute(self):
        # specific implementations for depositing money
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_no = ?', (self.amount, self.account_no))
        conn.commit()
        
        # fetch the updated balance from the database
        cursor.execute('SELECT balance FROM accounts WHERE account_no = ?', (self.account_no,))
        updated_balance = cursor.fetchone()[0] 
        
        conn.close()
        print("Deposit successful!")
        print("Your updated account balance is:", updated_balance)  # print the updated balance
