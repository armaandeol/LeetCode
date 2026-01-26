class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        output = []
        arr.sort()
        mini = float('inf')
        for i in range(len(arr)-1):
            num = abs(arr[i]-arr[i+1])
            if num < mini:
                output = []
                mini = num
                output.append([arr[i],arr[i+1]])
            elif num == mini:
                output.append([arr[i],arr[i+1]])
            else:
                pass
        return output