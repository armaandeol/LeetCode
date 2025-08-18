class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)

        words.sort(key=len)

        dp = [1] * n
        maxi = 1

        def compare(arr1,arr2):
            if len(arr1) !=  len(arr2) + 1:
                return False

            fst = 0
            snd = 0

            while fst < len(arr1):
                if snd < len(arr2) and arr1[fst] == arr2[snd]:
                    fst += 1
                    snd += 1
                else:
                    fst += 1

            return fst == len(arr1) and snd == len(arr2)

        for i in range(n):
            for prev_ind in range(i):
                if compare(words[i], words[prev_ind]) and 1 + dp[prev_ind] > dp[i]:
                    dp[i] = 1 + dp[prev_ind]

            if dp[i] > maxi:
                maxi = dp[i]

        return maxi
        