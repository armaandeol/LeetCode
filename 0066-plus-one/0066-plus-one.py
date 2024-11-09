class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = int(''.join(map(str, digits)))
    
        number += 1
        
        return [int(digit) for digit in str(number)]
        
        
        