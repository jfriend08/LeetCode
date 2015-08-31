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
      self.numberToWordsMap[1] = 'One'
      self.numberToWordsMap[2] = 'Two'
      self.numberToWordsMap[3] = 'Three'
      self.numberToWordsMap[4] = 'Four'
      self.numberToWordsMap[5] = 'Five'
      self.numberToWordsMap[6] = 'Six'
      self.numberToWordsMap[7] = 'Seven'
      self.numberToWordsMap[8] = 'Eight'
      self.numberToWordsMap[9] = 'Nine'
      self.numberToWordsMap[10] = 'Ten'
      self.numberToWordsMap[11] = 'Eleven'
      self.numberToWordsMap[12] = 'Twelve'
      self.numberToWordsMap[13] = 'Thirteen'
      self.numberToWordsMap[14] = 'Fourteen'
      self.numberToWordsMap[15] = 'Fifteen'
      self.numberToWordsMap[16] = 'Sixteen'
      self.numberToWordsMap[17] = 'Seventeen'
      self.numberToWordsMap[18] = 'Eighteen'
      self.numberToWordsMap[19] = 'Nineteen'
      self.numberToWordsMap[20] = 'Twenty'
      self.numberToWordsMap[30] = 'Thirty'
      self.numberToWordsMap[40] = 'Forty'
      self.numberToWordsMap[50] = 'Fifty'
      self.numberToWordsMap[60] = 'Sixty'
      self.numberToWordsMap[70] = 'Seventy'
      self.numberToWordsMap[80] = 'Eighty'
      self.numberToWordsMap[90] = 'Ninety'

    def getWords(self, num):
      digits = []
      testNum = num
      devide = 100
      while testNum > 0:
        digits.append(int(testNum/devide))
        testNum -= digits[-1] * devide
        devide = devide/10
        if testNum < 20 and testNum > 10:
          digits.append(testNum)
          break

      while len(digits) < 3:
        digits.append(0)

      result = []
      if digits[0] >0:
        result.append(self.numberToWordsMap[digits[0]] + ' Hundred')
      if digits[1] >0:
        try:
          result.append(self.numberToWordsMap[digits[1]*10])
        except:
          result.append(self.numberToWordsMap[digits[1]])
      if digits[2] >0:
        result.append(self.numberToWordsMap[digits[2]])
      return ' '.join(result)

    def numberToWords(self, num):
      if num == 0:
        return 'Zero'
      values = []
      testNum = num
      devide = 1000000000
      units = [' Billion', ' Million', ' Thousand', '']
      while testNum > 0:
        values.append(int(testNum/devide))
        testNum -= values[-1] * devide
        devide = devide/1000
      result = []
      for idx in range(len(values)):
        if values[idx] > 0:
          result.append(self.getWords(values[idx]) + units[idx])

      return ' '.join(result)

if __name__ == "__main__":
    test = Solution()
    print test.getWords(55)
    print test.getWords(132)
    print test.getWords(100)
    print test.getWords(101)
    print test.getWords(999)
    print test.getWords(001)
    print test.getWords(01)
    print test.getWords(123)
    print test.getWords(113)
    print test.numberToWords(100202)

