class Solution:
    def isHappy(self, n: int) -> bool:
      temp = set()
      while n != 1:
        if n in temp: return False
        temp.add(n)
        n =sum([int(i)**2 for i in str(n)])
      else :
         return  True