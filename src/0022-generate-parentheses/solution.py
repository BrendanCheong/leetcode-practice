class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Think of generating the parenthesis like a decision tree.
        if n = 2, we could do ( then ). Or we could do ( then (.
        Then for each closing bracket we have another decision.
        We can traverse this decision tree using bfs which uses queue or dfs which uses
        a stack.
                        (0, 0, '')
                            |	
                        (1, 0, '(')
                        /           \
                (2, 0, '((')      (1, 1, '()')
                    /                   \
            (2, 1, '(()')           (2, 1, '()(')
                /                           \
        (2, 2, '(())')                (2, 2, '()()')
                |	                         |
        res.append('(())')             res.append('()()')

        """
        res = []
        def dfs(left: int, right: int, s: str) -> str:
            # we formed our string when we reached n * 2 sized string
            if len(s) == n * 2:
                res.append(s)
                return

            # you start with the left bracket first
            # to form the parenthesis. its () not )(
            # less than 'n' means that we need n times of left bracket
            if left < n:
                dfs(left + 1, right, s + '(')
            # if too many left, we need to close the bracket
            if left > right:
                dfs(left, right + 1, s + ')')
        dfs(0, 0, '')
        return res

    def generateParenthesisIterative(self, n: int) -> List[str]:
        res = []
        left, right = 0, 0
        stack = [(left, right, '')]
        while stack:
            left, right, s = stack.pop()
            if len(s) == n * 2:
                res.append(s)
            if left < n:
                stack.append((left + 1, right, s + '('))
            if right < left:
                stack.append((left, right + 1, s + ')'))
        return res
            
