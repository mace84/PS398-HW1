# Matthias Orlowski
# 01/27/2012
# PS398 Homework 2
# Accounting program to keep track of cash, stock and mutual funds

import random

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
                
    def addCash(self,amount):
        self.cash = self.cash + amount

    def withdrawCash(self, amount):
        self.balance = self.balance - amount

    def buyStock(self, stock):
        if isinstance(stock,dict) == False:
            print "This function allows you to add stocks to your portfolio. Your input is not a stock. Please create one using the Stock() function first."
        stock

    def CommunistsAreComing(self):
            print """You are to rich!
            You are taxed 50% of your cash, stocks and mutual funds
            for building sewage systems, roads, and kindergartens.
            We know you always like to help!
            \n
            Your Government."""
            
            self.cash = self.cash - self.cash*.5
            self.stock = self.stock - self.stock/2
            self.mutual_funds = self.mutual_funds-self.mutual_funds*.5
    
class FinInstr(object):

    def __init__(self, label):
        self.name = label
        
class Stock(FinInstr):

    def __init__(self,buy_price):
        self.pricebought = buy_price
        self.pricesold = random.uniform(0.5*self.pricebought, 1.5*self.pricebought)

class MutualFund(FinInstr):

    def __init__(self,shares):
        self.sharesheld = shares
        self.pricesold = random.uniform(0.9,1.2)

