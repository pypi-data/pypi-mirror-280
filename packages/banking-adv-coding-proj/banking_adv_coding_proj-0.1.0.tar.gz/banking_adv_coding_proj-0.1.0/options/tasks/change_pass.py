from options.tasks.account_action import AccountAction
from options.tasks.password import PasswordManager

# child class: ChangePassword inherits from the parent class: AccountAction
class ChangePassword(AccountAction):
    def __init__(self, account_no, new_password):
        # initializing the parent class with account number
        super().__init__(account_no)
        self.new_password = new_password

    def execute(self):
        # using PasswordManager to change the password
        PasswordManager(self.account_no).change_password(self.new_password)
