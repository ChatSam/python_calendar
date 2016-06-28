
class BankAccount(object) :
  balance = 0;

  def __init__(self,name):
    self.name = name;

  def __repr__(self):
    return "Account belongs to %s. The balance in the account is $%.2f" % (self.name,self.balance)

  def show_balance(self):
    print "Balance : $ %.2f " % (self.balance)

  def deposit(self,amount):
    if amount <= 0:
      print "Invalid amount entered";
    else:
      print "balance prior to deposit %.2f" % (self.balance)
      self.balance += amount;
      self.show_balance();

  def withdraw(self, amount):
    if amount > self.balance:
      print "Error. The amount exceeds the available balance"
    else:
      print "User is withdrawing $%.2f" % (amount)
      self.balance -= amount;

my_account = BankAccount("Samare");

print my_account;

my_account.show_balance();

my_account.deposit(2000);
my_account.withdraw(1000);
print my_account;

