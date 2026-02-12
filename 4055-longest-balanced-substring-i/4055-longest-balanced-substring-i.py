class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = {}
            max_freq = 0
            
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                max_freq = max(max_freq, freq[char])
                
                distinct = len(freq)
                length = j - i + 1
                
                if length == distinct * max_freq:
                    max_len = max(max_len, length)
        
        return max_len
