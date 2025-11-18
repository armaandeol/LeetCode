class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        status = True
        while status:
            if i == len(bits) - 1 and bits[i] == 0:
                return True
            elif i > len(bits) - 1:
                return False
            if bits[i] == 1:
                i += 2
            else:
                i += 1