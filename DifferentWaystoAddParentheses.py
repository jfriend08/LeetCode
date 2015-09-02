'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution(object):
    def __init__(self):
      self.allSol = []
    def nextIdxFromI(self, i, string):
      for idx in range(i+1,len(string)):
        if string[idx] == '+' or string[idx] == '-' or string[idx] == '*':
          return idx +1

    def isValidString(self, string):
      count_normal = 0
      count_neg = 0
      for idx in range(len(string)):
        if string[idx] == '+' or string[idx] == '*':
          count_normal += 1
        elif [idx] == '-':
          count_neg += 1
      return count_normal >0 or count_neg > 1

    def calculate (self, string):
      if len(string) != 3:
        if string[0] == '-':
          val1 = -int(string[1])
          opt = string[2]
          val2 = int(string[3])
        else:
          val1 = int(string[0])
          opt = string[1]
          val2 = -int(string[3])
      else:
        val1 = int(string[0])
        opt = string[1]
        val2 = int(string[2])
      if opt == '+':
        return str(val1 + val2)
      elif opt == '-':
        return str(val1 - val2)
      elif opt == '*':
        return str(val1 * val2)
      else:
        return

    def diffWaysToCompute(self, input):
      print input
      size = len(input)
      print self.isValidString(input)
      if self.isValidString(input):
        self.allSol.append(input)
      newStrings = []
      i = 0
      while i < size-2:
        if input[i+2] == '-' or input[0] == '-':
          j = i+4
        else:
          j = i+3
        sub = input[i:j]
        newStrings.append(input[0:i] + self.calculate(sub) + input[j:size])
        i = self.nextIdxFromI(i, input)
      print newStrings
      map(self.diffWaysToCompute, newStrings)
      return self.allSol

if __name__ == "__main__":
    test = Solution()
    print 'result: %s' % test.diffWaysToCompute("2*3-4*5")
    print 'result: %s' % test.diffWaysToCompute("2*-3-4*5")




