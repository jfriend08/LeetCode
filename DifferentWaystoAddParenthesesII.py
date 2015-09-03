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
    def diffWaysToCompute(self, input):
      if input.isdigit():
        return [int(input)]
      result = []
      for idx in xrange(len(input)):
        if input[idx] in '+-*':
          res1 = self.diffWaysToCompute(input[:idx])
          opt = input[idx]
          res2 = self.diffWaysToCompute(input[idx+1:])
          for i in res1:
            for j in res2:
              result.append(self.calculate(i, opt, j))
              print result
      return result

    def calculate(self, res1, opt, res2):
      if opt == '+':
        return res1 + res2
      elif opt == '-':
        return res1 - res2
      elif opt == '*':
        return res1 * res2

if __name__ == "__main__":
    test = Solution()
    print 'result: %s' % test.diffWaysToCompute("2*3-4*5")
