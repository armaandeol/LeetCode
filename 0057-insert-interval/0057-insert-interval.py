class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        ques = [intervals[0]]

        for i in range(1, len(intervals)):
            if ques[-1][1] >= intervals[i][0]:
                ques[-1][1] = max(ques[-1][1], intervals[i][1])
            else:
                ques.append(intervals[i])

        return ques