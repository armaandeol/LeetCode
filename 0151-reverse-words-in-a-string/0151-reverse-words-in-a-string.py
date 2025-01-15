class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(' ') if word]
        words.reverse()

        return ' '.join(words)