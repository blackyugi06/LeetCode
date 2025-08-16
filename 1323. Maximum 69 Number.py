class Solution:
    def maximum69Number (self, num: int) -> int:
        S = str(num)
        if S.count('6') != 0 :
            S = S[:S.find('6')] + '9' + S[S.find('6')+1:]
        return int(S)
