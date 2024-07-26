class BankAccount:
  def __init__(self, initial_balance=0):
    self.account_balance = initial_balance
  def deposit (self,amount):
    if amount > 0:
        self.account_balance += amount
  def withdraw (self,amount):
    if self.account_balance != 0:
      self.account_balance -= amount
      return True
    else:
      print(f"Insufficient funds.")
      return False
  def display_balance(self):
    print(f"Current Balance: ${self.account_balance:.2f}")

