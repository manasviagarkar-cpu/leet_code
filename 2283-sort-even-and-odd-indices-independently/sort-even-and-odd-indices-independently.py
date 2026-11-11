class Solution:
    def sortEvenOdd(self, A: list[int]) -> list[int]:
        e = []
        o = []
        for i in range(len(A)):
            if i %2==0:
                e.append(A[i])
            else :
                o.append(A[i])
        e.sort()
        o.sort(reverse = True)
        B=[]
        for i in range(len(o)):
            B.append(e[i])
            B.append(o[i])
        o_len=len(o)
        e_len =len(e)
        if o_len > e_len:
            B.extend(o[e_len:])
        if e_len > o_len:
            B.extend(e[o_len:])
        return B

        