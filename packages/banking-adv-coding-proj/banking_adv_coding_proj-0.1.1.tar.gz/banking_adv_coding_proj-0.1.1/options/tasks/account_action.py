import sqlite3

class AccountAction: # this is the parent class (or base class) for all account-related actions
    def __init__(self, account_no):
        self.account_no = account_no

    def execute(self):
        # method should be implemented by all subclasses
        raise NotImplementedError("Subclasses should implement this method")

    def get_account(self):
        # to fetch account details from the database
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE account_no = ?', (self.account_no,))
        account = cursor.fetchone() # retrieve one row
        conn.close()
        return account
    



