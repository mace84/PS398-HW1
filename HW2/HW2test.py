# Matthias Orlowski
# 01/27/2012
# PS398 Homework 2
# Test for accounting program
import unittest
import HW2

class TestHWAccounting(unittest.TestCase):
    def selfUp(self):
        return

# test for negative numbers
# check what happens after passing more than two digits
# check what happens when passing integers instead of floating points


 #portfolio = Portfolio() Creates a new portfolio

#portfolio.addCash(300.50) Adds cash to the portfolio
def test_addCash():

# s = Stock(20, "HFH") Create Stock with price 20 and symbol "HFH"

# portfolio.buyStock(5, s) Buys 5 shares of stocks
def buyStock():

# portfolio.sellStock("HFH", 1) #Sells 1 share of HFH 

# mf1 = MutualFund(5, "BRT") Create MF with price 5 and symbol "BRT"

# mf2 = MutualFund(2, "GHT") Create MF with price 2 and symbol "GHT" 

# portfolio.buyMutualFund(10.3, mf1) Buys 10.3 shares of "BRT"

# portfolio.buyMutualFund(2, mf2) Buys 2 shares of "GHT"

# print(portfolio) # Prints portfolio
#                       cash: $140.50
#                       stock: 5 HFH
#                       mutual funds: 10.33 BRT
#                                     2     GHT
    
# portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT


# portfolio.withdrawCash(50) #Removes $50
def withdrawCash():

# portfolio.history() #Prints a list of all transactions ordered by time

if __name__ == '__main__':
    unittest.main()


reload(HW2)
acc=HW2.Portfolio("ACC",600)
st1 = HW2.Stock(10,"st1")
st2 = HW2.Stock(20,"st2")
mf1 = HW2.MutualFund("mf1")
mf2 = HW2.MutualFund("mf2")

acc.buyStock(10,st1)
acc.buyMutualFund(70,mf1)
acc.buyMutualFund(30,mf2)
acc.sellMutualFund("mf1",20)
acc.buyStock(10,st2)

acc.addCash(120)
acc.buyStock(10,st2)
acc.withdrawCash(70)
acc.withdrawCash("30")
acc.sellStock("st1",5)
acc.sellStock("st2",10)
acc.buyMutualFund(70,mf1)
acc.buyMutualFund(10.124,mf1)
print(acc)
