class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        characters = set(word)
        dummy_characters = characters.copy()
        for i in characters:
            dummy_characters.remove(i)
            if i.lower() in dummy_characters or i.upper() in dummy_characters:
                count += 1
        return count 
