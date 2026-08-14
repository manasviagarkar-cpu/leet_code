class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left , right = 0 , len(s)-1
        vowels =['a','e','i','o','u','A','E','I','O','U']
        if len(s)==0:
            return s
        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)