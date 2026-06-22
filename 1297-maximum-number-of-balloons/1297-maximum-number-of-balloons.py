class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {}
        for i in text:
            if i not in hashmap:
                hashmap[i]  = 1
            else:
                hashmap[i] += 1
        
        return min(hashmap.get('b',0),hashmap.get('a',0),hashmap.get('l',0) // 2,hashmap.get('o',0)//2,hashmap.get('n',0))
    