class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2

        full_sum = sum(nums)
        half_sum = full_sum // 2

        if sum(nums[:half]) == half_sum or sum(nums[half:]) == half_sum:
            return full_sum - 2 * half_sum

        def get_subsets_sums(elems):
            result = defaultdict(set)
            result[0] = {0}
            for elem in elems:
                for cnt in reversed(list(result)):
                    result[cnt + 1].update(value + elem for value in result[cnt])
            return result

        left = get_subsets_sums(nums[:half])
        right = get_subsets_sums(nums[half:])

        def calc(left,right):
            result = min(min(left[half]), min(right[half]))

            for left_cnt, left_sums in left.items():
                right_cnt = half - left_cnt
                right_sums = right[right_cnt]

                a = sorted(left_sums)
                b = sorted(right_sums)
                m = len(a)
                l = len(b)
                i = 0
                j = l - 1

                while i<m and j >= 0:
                    current = a[i] +  b[j]
                    if current == half_sum:
                        return full_sum - 2 * current 
                    if current > half_sum:
                        j -= 1
                    else:
                        result = max(result, current)
                        i += 1

            return full_sum - 2 * result

        return calc(left,right)