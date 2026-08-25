import math 
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        q = [int(char) for char in str(n)]
        p = math.prod(q)
        s = sum(q)
        return p-s
        