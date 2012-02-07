# Matthias Orlowski
# 01/27/2012
# PS398 Homework 2
# Accounting program to keep track of cash, stock and mutual funds

#!/usr/bin/python

import random
import datetime
        
class Portfolio(object):

# define portfolio content
    def __init__(self,account,cash=0,funds = {}, fund_sellprices ={}, stock = {}, stock_buyprices = {},stock_sellprices = {}, log = ""):
        self.account = str(account) # kind of unnecessary
        self.cash = cash
	self.mutual_funds = {}
        self.fund_sellprices = {}
        self.stock = {}
        self.stock_buyprices = {} # not necessary now but if one would want to include margins in output
        self.stock_sellprices = {}        
        self.log = log
        
        if self.cash > 500:
            self.CommunistsAreComing()
            
# define print(portfolio)
    def __str__(self):
        temp1 = str(self.stock)
        temp1 = temp1.rstrip("}")
        temp1 = temp1.strip("{")
        temp1 = temp1.rsplit(",")
        stocklist = "\n "
        for i in range(0,len(temp1)):
            stocklist = stocklist + temp1[i] + "\n"
        temp2 = str(self.mutual_funds)
        temp2 = temp2.rstrip("}")
        temp2 = temp2.strip("{")
        temp2 = temp2.rsplit(",")
        fundlist = "\n "
        for i in range(0,len(temp2)):
            fundlist = fundlist + temp2[i] + "\n"

        output = """Account: %s

Cash: $%d

Stocks: %s
Mutual Funds: %s
""" %(self.account,self.cash,stocklist,fundlist)
        print output
        
# Transaction functions (warnings and input checks are not DRY! make functions for both.)
    def addCash(self,amount):
        if isinstance(amount,int)== False and isinstance(amount,float) == False:
            if amount.isdigit() == False:
                return "WARNING! \nPlease enter a positive number with at most two digits indicating your deposit. \nFor withdraws use the withdrawCash() function."
        amount = float(amount)
        if amount <= 0:
            return "WARNING! \nPlease enter a positive number with at most two digits indicating your deposit. \nFor Withdraws use the withdrawCash() function."

        self.cash = self.cash + amount
        entry = "cash deposit: $" + str(amount)
        self.LogEntry(entry)
        
        if self.cash > 500:
            self.CommunistsAreComing()


    def withdrawCash(self, amount):
        if isinstance(amount,int)== False and isinstance(amount,float) == False:
            if amount.isdigit() == False:
                return "WARNING! \n Please enter a positive number with at most two digits indicating your withdraw."
        amount = float(amount)
        if amount <= 0:
            return "WARNING! \n Please enter a positive number with at most two digits indicating your withdraw."

        if self.cash < amount:
            return "We are sorry, but you cannot afford to withdraw this much. Your curren balance is: $%d. \nPlease choose a smaller amount for withdraw or talk to your financial consultant about the possibility to take out loans." % self.cash
        self.cash = self.cash - amount
        entry = "cash withdraw: $" + str(amount)
        self.LogEntry(entry)


    def buyStock(self, number, stock):
        # if isinstance(stock,HW2.Stock) == False:
        #     return "This function allows you to add stocks to your portfolio. Your input is not a stock. Please create one using the Stock() function first."
        if isinstance(number,int) == False:
            return "Stock can only be purchased or sold as whole units. Please enter an integer value indicating the number of units you would like to trade."

        if self.cash < stock.pricebought*number:
            return "We are sorry, but you cannot afford these stocks. Please choose a lower number of units for purchase or talk to your financial consultant about the possibility to take out loans."
        
        if self.stock.has_key(stock.name) == True:
            self.stock[stock.name] = number + self.stock[stock.name]
            
        else:        
            self.stock[stock.name] = number
            self.stock_buyprices[stock.name] = stock.pricebought
            self.stock_sellprices[stock.name] = stock.pricesold
            
        self.cash = self.cash - stock.pricebought*number
        entry = str(number) + " " + str(stock.name) + " stocks bought for: $" + str(stock.pricebought*number)
        self.LogEntry(entry)


    def sellStock(self, key, number):
        if isinstance(number,int) == False:
            return "Stock can only be purchased or sold as whole units. Please enter an integer value indicating the number of units you would like to trade."

        if self.stock.has_key(key) == False or self.stock[key] == 0:
            return "We are sorry, but you don't own any of these stock. you can buy them by using the buyStock() function."
         
        self.stock[key] = self.stock[key] - number
        self.cash = self.cash + self.stock_buyprices[key]*number
        entry = str(number) + " " + str(key) + " stocks sold for: $" + str(self.stock_buyprices[key]*number)
        self.LogEntry(entry)

        if self.cash > 500:
            self.CommunistsAreComing()


    def buyMutualFund(self,share,fund):
        if self.cash < share:
            return "We are sorry, but you cannot afford these mutual funds. Please choose a lower share for purchase or talk to your financial consultant about the possibility to take out loans."

        if share > fund.instock:
            return "You cannot buy more than 100 shares. The maximum you can buy is %d and %d is the maximum you could currently afford." %(fund.instock,self.cash)
            
        if self.mutual_funds.has_key(fund.name) == True:
            self.mutual_funds[fund.name] = share + self.mutual_funds[fund.name]
            
        else:        
            self.mutual_funds[fund.name] = share            
            self.fund_sellprices[fund.name] = fund.pricesold
    
        self.cash = self.cash - share
        fund.instock = fund.instock - share
        entry = str(share) + " shares in " + str(fund.name) + " bought for: $" + str(share)
        self.LogEntry(entry)


    def sellMutualFund(self, key, share):
        if share > 100:
            return "Stock can only be purchased or sold as whole units. Please enter an integer value indicating the number of units you would like to trade."

        if self.mutual_funds.has_key(key) == False or self.mutual_funds[key] < share:
            return "We are sorry, but you don't own enough of this fund. You can buy it using the buyMutualFund() function or lower the number of shares you want for sale."
        
        self.mutual_funds[key] = self.mutual_funds[key] - share
        self.cash = self.cash + share*self.fund_sellprices[key]
        entry = str(share) + " shares in " + str(key) + " sold for: $" + str(share*self.fund_sellprices[key])
        self.LogEntry(entry)
        if self.cash > 500:
            self.CommunistsAreComing()


    def CommunistsAreComing(self):
            print """You are too rich!
You are taxed 50% of your cash, for building sewage systems, roads, and kindergartens. Stocks and mutual funds are not taxed until they are sold. So better think twice when cashing in your investments!
But after all, we know you always like to help!
\n
Your Government."""
            
            self.cash = self.cash - self.cash*.5


    def LogEntry(self,entry):
        now = datetime.datetime.now()
        temp = now.strftime("%Y-%m-%d %H:%M") + ": " + entry + " \n"
        self.log = self.log + temp


    def history(self):
        print self.log
    
# Stocks and Mutual Funds
class Stock(object):

    def __init__(self,buy_price,label,pricesold=0):
        self.name = label       
        self.pricebought = buy_price
        self.pricesold = random.uniform(0.5*self.pricebought, 1.5*self.pricebought)
    def __str__(self):
        output = "STOCK \nName: " + str(self.name) + "\nBought at: $" + str(self.pricebought) + "\nSell for: $" + self.pricesold
        print output


class MutualFund(object):

    def __init__(self,label,pricesold=0, instock=100.0):
        self.name = label
        self.pricesold = random.uniform(0.9,1.2)
        self.instock = instock

    def __str__(self):
        output = "MUTUAL FUND \nName: " + str(self.name) + "\nShares for sale: " + format(self.instock,'.0f')
        print output

