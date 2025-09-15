class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        sequence = text.split(" ")
        for i in sequence:
            status = True
            for j in i:
                if j in brokenLetters:
                    status = False
            if status:
                count += 1


        return count 