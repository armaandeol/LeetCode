class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a = -1
        b = -1
        result = 0

        for start, end in intervals:
            if b < start:
                a = end - 1
                b = end
                result += 2
            elif a < start:
                a = b
                b = end
                result += 1


        return result