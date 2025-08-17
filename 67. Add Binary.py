class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = len(a)
        B = len(b)
        if A < B:
            a, b = b, a
            A, B = B, A
        b = "0" * (A - B) + b
        carry = 0
        ans = [None] * A
        for i in range(A - 1, -1, -1):
            bt = (carry + int(a[i]) + int(b[i]))
            carry = int(bt > 1)
            ans[i] = str(bt % 2)
        a = "".join(ans)
        if carry:
            a = "1" + a
        return a
