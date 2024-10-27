class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        summ = int(''.join(map(str, digits)))
    
        summ += 1
        
        return [int(digit) for digit in str(summ)]
        
        
        