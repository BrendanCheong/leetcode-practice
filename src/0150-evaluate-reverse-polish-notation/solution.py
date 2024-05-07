class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Rather simple solution, since we're always guaranteed to have 2 numbers to
        use an operator on.

        Trick is the divide part, we don't want float numbers so we need to int(num2 / num1)
        Also its num2 divide num1, as its LIFO, as we notice we use the first in number
        to divide the last out

        Time: O(n)
        Space: O(n)
        """
        operators = {'+', '-', '*', '/'}
        stack = []
        for i, tok in enumerate(tokens):
            if tok not in operators:
                stack.append(int(tok))
            else:
                num1, num2 = stack.pop(), stack.pop()
                if tok == '+':
                    new_num = num2 + num1
                elif tok == '*':
                    new_num = num2 * num1
                elif tok == '/':
                    new_num = int(num2 / num1)
                else:
                    new_num = num2 - num1
                stack.append(new_num)
        return stack[-1]
        
