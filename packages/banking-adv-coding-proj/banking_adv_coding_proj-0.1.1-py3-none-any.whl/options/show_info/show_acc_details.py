from options.tasks.account_action import AccountAction
import sqlite3

# childclass: ShowAccountDetails inherits from the parent class: AccountAction
class ShowAccountDetails(AccountAction):
    def execute(self):
        # specific implementation for showing account details.
        account = self.get_account()
        if account:
            print(f"Holder Name: {account[3]}, Account No: {account[0]}, Password: {account[1]}, Balance: {account[2]}") # using f string to format the string
        else:
            print("Account not found.")
