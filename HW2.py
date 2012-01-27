# Matthias Orlowski
# 01/27/2012
# PS398 Homework 2
# Accounting program to keep track of cash, stock and mutual funds

def Stock(self, price, label):
    watchlist[label] = price

class Portfolio(object):
    
    def __init__(self,account,cash=0, stock=0, funds=0, watch = {}):
        self.account = account
        self.cash = cash
      	self.stock = stock
	self.mutual_funds = funds
        self.balance = self.cash + self.stock + self.mutual_funds
        self.watchlist = watch
        
    def Balance(self):
        print "Account:", self.account
        print "Balance:", self.cash
        
    def addCash(self,amount):
        self.cash = self.cash + amount

    def withdrawCash(self, amount):
        self.balance = self.balance - amount

    def buyStock(self, stock):
        if isinstance(stock,dict) == False:
            print "This function allows you to add stocks to your portfolio. Your input is not a stock. Please create one using the Stock() function first."
        stock
        
