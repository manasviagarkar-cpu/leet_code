class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse = True)
        res = []
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        odd_len = len(odd)
        even_len = len(even)
        if odd_len > even_len:
            res.extend(odd[even_len:])
        if even_len > odd_len:
            res.extend(even[odd_len:])
        return res