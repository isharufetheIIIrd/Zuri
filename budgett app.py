class budget:
  def __init__(self, category):                                        
        self.Register =[]
        self.amount=0
        self.category = category 

#checks if theres money
  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True


  def deposit(self,amount):
    amt = int(input("how much do you want to deposit: "))
    self.amount += amt


  def withdraw(self,amount):
    amountw = int(input("how much do you want to withdraw: "))
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.Register.append({"amount":-amount})
      return True
    else:
      return False

  # return balance of budget 
  def get_balance(self):
    return self.amount


#transfer methos which takes in amount and category name as arguments
#appends to register account transferred from and transferred to

  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.Register.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False





 
#instantiating categories
food= budget('food')
clothing = budget("clothing")
entertainment = budget("entertainment")




