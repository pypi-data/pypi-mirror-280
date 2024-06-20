import sqlite3
from options.tasks.account_action import AccountAction

# child class: Withdraw inherits from the parent class: AccountAction
class Withdraw(AccountAction):
    def __init__(self, account_no, amount):
        # initializing the parent class with account number
        super().__init__(account_no)
        self.amount = amount

    def execute(self):
        # specific implementations for withdrawing money
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM accounts WHERE account_no = ?', (self.account_no,))
        balance = cursor.fetchone()[0]
        
        if balance >= self.amount:
            # update the balance in the database
            new_balance = balance - self.amount
            cursor.execute('UPDATE accounts SET balance = ? WHERE account_no = ?', (new_balance, self.account_no))
            conn.commit()
            print("Withdrawal successful!")
            print("Your updated account balance is: ", new_balance)  # Print the updated balance
        else:
            print("Insufficient balance.")
        
        conn.close()

