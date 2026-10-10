class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            carry = 0
            for i in range(len(digits)-1, -1, -1):
                if digits[i]+carry == 10 or (i==len(digits)-1 and digits[i]+1==10):
                    digits[i]=0
                    carry = 1
                else:
                    digits[i]+=carry
                    carry = 0
        if carry == 1:
            digits.insert(0,1)
        return digits
        