'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
'''

class Solution(object):
    def __init__(self):
      self.numberToWordsMap = {}
      self.numberToWordsMap[0] = ''
      self.numberToWordsMap[1] = 'One '
      self.numberToWordsMap[2] = 'Two '
      self.numberToWordsMap[3] = 'Three '
      self.numberToWordsMap[4] = 'Four '
      self.numberToWordsMap[5] = 'Five '
      self.numberToWordsMap[6] = 'Six '
      self.numberToWordsMap[7] = 'Seven '
      self.numberToWordsMap[8] = 'Eight '
      self.numberToWordsMap[9] = 'Nine '
      self.numberToWordsMap[10] = 'Ten '
      self.numberToWordsMap[11] = 'Eleven '
      self.numberToWordsMap[12] = 'Twelve '
      self.numberToWordsMap[13] = 'Thirteen '
      self.numberToWordsMap[14] = 'Fourteen '
      self.numberToWordsMap[15] = 'Fifteen '
      self.numberToWordsMap[16] = 'Sixteen '
      self.numberToWordsMap[17] = 'Seventeen '
      self.numberToWordsMap[18] = 'Eighteen '
      self.numberToWordsMap[19] = 'Nineteen '
      self.numberToWordsMap[20] = 'Twenty '
      self.numberToWordsMap[30] = 'Thirty '
      self.numberToWordsMap[40] = 'Fourty '
      self.numberToWordsMap[50] = 'Fifty '
      self.numberToWordsMap[60] = 'Sixty '
      self.numberToWordsMap[70] = 'Seventy '
      self.numberToWordsMap[80] = 'Eighty '
      self.numberToWordsMap[90] = 'Ninty '

    def getWords(self, num):
      digits = []
      testNum = num
      devide = 100
      while testNum > 0:
        digits.append(int(testNum/devide))
        testNum -= digits[-1] * devide
        devide = devide/10
      if num >= 100:
        try:
          print '%sHundred %s%s' % (self.numberToWordsMap[digits[0]], self.numberToWordsMap[digits[1]*10], self.numberToWordsMap[digits[2]])
        except:
          print '%sHundred' % (self.numberToWordsMap[digits[0]])
      elif num >= 10:
        print '%s%s' % (self.numberToWordsMap[digits[1]*10], self.numberToWordsMap[digits[2]])
      else:
        print '%s' % (self.numberToWordsMap[digits[2]])

    def numberToWords(self, num):
      if num<1000:
        getWords(num)

if __name__ == "__main__":
    test = Solution()
    test.getWords(55)
    test.getWords(132)
    test.getWords(100)
    test.getWords(101)
    test.getWords(999)
    test.getWords(001)
    test.getWords(01)
    test.getWords(1)

