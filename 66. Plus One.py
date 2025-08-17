class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        for i, x in enumerate(digits):
            if x != 9:
                digits[i] += 1
                digits[:i] = [0] * i
                return digits[::-1]
        return [1] + [0] * len(digits)
        
