# Computation in Social Sciences
# Matthias Orlowski
# Homework 1
# 01/24/12
# Unit tests for Homework script
import unittest
import HW1

class TestHomeWorkCode(unittest.TestCase):

    def setUp(self):
        return

# shout(str) - Takes a string as an argument and returns a shouted version of that string (all caps with an exclamation point)
    def test_ShoutCapital(self):
        self.assertEqual(HW1.shout("Something wrong"), "SOMETHING WRONG!")
    def test_ShoutPunct(self):
        self.assertEqual(HW1.shout("Something wrong? Yes. No! Maybe"), "SOMETHING WRONG! YES! NO! MAYBE!")
    def test_ShoutNostr(self):
        self.assertEqual(HW1.shout(1), "")
        

# reverse(str) - Takes a string and reverses all of the characters in the string   
    def test_Reverse(self):
        self.assertEqual(HW1.reverse("123 456."),".654 321")
    def test_ReverseNostr(self):
        self.assertEqual(HW1.reverse(1),"")
        
# reversewords(str) - Takes a string and reverses the word order in each sentence
    def test_Reversewords(self):
        self.assertEqual(HW1.reversewords("one two three. four five."),"three two one. five four.")
    def test_ReversewordsPunct(self):
        self.assertEqual(HW1.reversewords("one two three. four five"),"three two one. five four.")
    def test_ReversewordsNostr(self):
        self.assertEqual(HW1.reversewords(1),"")
        
# reversewordletters(str) - Takes a string and reverses the letters in each word
    def test_Reversewordletters(self):
        self.assertEqual(HW1.reversewordletters("one two three. four five."),"eno owt eerht. ruof evif.")
    def test_ReversewordlettersPunct(self):
        self.assertEqual(HW1.reversewordletters("one two three. four five"),"eno owt eerht. ruof evif.")

if __name__ == "__main__":
        unittest.main()
