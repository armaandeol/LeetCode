class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(a, b):
            if len(a) != len(b):
                return False

            return sorted(a) == sorted(b)
        output = list(words)
        i = 1
        while i < len(output):
            if is_anagram(output[i - 1], output[i]):
                output.pop(i)
            else:
                i += 1
        return output
