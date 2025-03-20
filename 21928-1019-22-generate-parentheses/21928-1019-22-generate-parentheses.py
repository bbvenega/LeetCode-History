class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l: int,r: int,s: str):
            # print(f"In dfs with l: {l} r: {r} and s:{s}")
            if n * 2 == len(s):
                ans.append(s)
                return

            if l < n:
                dfs(l + 1,r, s + '(')
            
            if r < l:
                dfs(l,r + 1,s + ')')

        ans = []

        dfs(0, 0, "")
        return ans

