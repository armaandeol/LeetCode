class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        brokenUsers = set()
        
        for (u, v) in friendships:
            if set(languages[u-1]).isdisjoint(languages[v-1]):
                brokenUsers.add(u)
                brokenUsers.add(v)

        if not brokenUsers:
            return 0

        count = [0] * (n + 1)
        for user in brokenUsers:
            for lang in languages[user - 1]:
                count[lang] += 1

        maxKnown = max(count)

        return len(brokenUsers) - maxKnown
