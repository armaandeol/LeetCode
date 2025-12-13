class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        inactive = [i for i in range(len(code)) if not isActive[i]]

        for idx in sorted(inactive, reverse=True):
            code.pop(idx)
            businessLine.pop(idx)
        
        my_dict = {}
        for i in range(len(code)):
            if not re.fullmatch(r"[A-Za-z0-9_]+", code[i]):
                continue

            my_dict.setdefault(businessLine[i], []).append(code[i])

        result = []
        for category in ['electronics', 'grocery', 'pharmacy', 'restaurant']:
            if category in my_dict:
                my_dict[category].sort()
                result.extend(my_dict[category])

        return result