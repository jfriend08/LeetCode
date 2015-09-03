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
          if string[idx+1] == '+' or string[idx+1] == '-' or string[idx+1] == '*':
            return idx + 2
          return idx + 1

    def isValidString(self, string):
      hasSignAtFront = string[0] == '-' or string[0] == '+' or string[0] == '*'
      for idx in range(1,len(string)):
        hasSignAtBack = string[idx] == '-' or string[idx] == '+' or string[idx] == '*'
        if hasSignAtBack:
          break

      if hasSignAtFront and hasSignAtBack:
        return True
      elif not hasSignAtFront and hasSignAtBack:
        return True
      elif not hasSignAtFront and not hasSignAtBack:
        return False
      else:
        return False
    def findOptIdxFromI(i,string):
      for idx in range(i, len(string)):
        if string[idx] == '-' or string[idx] == '+' or string[idx] == '*':
          return idx
    def calculate (self, string):
      if len(string) != 3:
        if string[0] == '-':
          j = self.findOptIdxFromI(1,string)
          val1 = -int(string[1:j])
          opt = string[j]
          val2 = int(string[j+1:len(string)])
        else:
          j = self.findOptIdxFromI(0,string)
          val1 = int(string[0:j])
          opt = string[j]
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
      print 'input: %s'%input
      size = len(input)
      print self.isValidString(input)
      if not self.isValidString(input):
        print 'append'
        self.allSol.append(input)
      else:
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
    print '--------------------'
    print 'result: %s' % test.diffWaysToCompute("2*-3-4*5")




