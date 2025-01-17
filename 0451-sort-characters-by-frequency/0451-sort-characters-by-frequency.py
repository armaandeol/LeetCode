class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        ans = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = []
        for char, count in ans:
            result.append(char * count)

        return ''.join(result)
