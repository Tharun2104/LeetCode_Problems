"""
150. Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

"""
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []
        operators = {
            "+" : lambda y, x: x + y,
            "-" : lambda y, x: x-y,
            "*" : lambda y, x: x*y,
            "/" : lambda y, x: int(x/y)
        }
        for i in tokens:
            try:
                i = int(i)
                stk.append(int(i))
            except ValueError as ve:
                x = stk.pop()
                y = stk.pop()
                stk.append(operators[i](x,y))
        return stk[-1]

# Tip : can handle negative values with condition len(token) > 1 or token.isdigit():

tst = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Solution().evalRPN(tst)
