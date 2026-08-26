class Solution:
    def countDigits(self, num: int) -> int:
        q=sorted([int(char) for char in str(num)])
        count = 0
        for i in range(0,len(q)):
            if num % q[i] == 0 :
                 count += 1
            else :
                count 
        return count
    

        