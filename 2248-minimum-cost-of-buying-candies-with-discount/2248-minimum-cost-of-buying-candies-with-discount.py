class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        stack = []
        cost.sort()
        while cost:
            stack.append(cost.pop())
            if len(stack) >= 2:
                total += sum(stack)
                while stack:
                    stack.pop()
                if cost:
                    cost.pop()
        while stack:
            total += stack.pop()
        return total