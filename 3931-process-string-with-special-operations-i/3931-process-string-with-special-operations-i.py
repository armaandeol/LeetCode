class Solution:
    def processStr(self, s: str) -> str:
        special = ["#", "*", "%"]
        result = []
        for i in s:
            if i in special:
                if result:
                    if i == "#":
                        result.extend(result)
                    elif i == "*":
                        result.pop()
                    else:
                        result.reverse()

                else:
                    continue
                
            else:
                result.append(i)
        return ''.join(result)