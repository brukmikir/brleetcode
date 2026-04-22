class Solution:
    def diffWaysToCompute(self, expression: str):
        
        memo = {}
        
        def solve(s):
            if s in memo:
                return memo[s]
            
            res = []
            
            for i in range(len(s)):
                if s[i] in "+-*":
                    left = solve(s[:i])
                    right = solve(s[i+1:])
                    
                    for a in left:
                        for b in right:
                            if s[i] == '+':
                                res.append(a + b)
                            elif s[i] == '-':
                                res.append(a - b)
                            else:
                                res.append(a * b)
            
            if not res:
                res = [int(s)]
            
            memo[s] = res
            return res
        
        return solve(expression)