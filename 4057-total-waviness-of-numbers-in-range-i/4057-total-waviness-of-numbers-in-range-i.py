class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        if num2 < 100:
            return waviness
        def check(num,waviness):
            digit_list = [int(x) for x in str(num)]
            for i in range(1,len(digit_list)-1):
                if digit_list[i] > digit_list[i-1] and digit_list[i] > digit_list[i+1]:
                    waviness += 1
                elif digit_list[i] < digit_list[i-1] and digit_list[i] < digit_list[i+1]:
                    waviness += 1
            return waviness
        for num in range(num1,num2+1):
            waviness = check(num,waviness)
        return waviness