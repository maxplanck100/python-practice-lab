class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_num, balance=0):
        self.accounts[acc_num] = balance

    def transaction(self, acc_num, amount):
        if acc_num in self.accounts and self.accounts[acc_num] + amount >= 0:
            self.accounts[acc_num] += amount
            return True
        return False
