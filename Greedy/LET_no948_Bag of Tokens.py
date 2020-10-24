class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        res = cur = 0
        queue = collections.deque(sorted(tokens))
        while queue and (P >= queue[0] or cur != 0):
            if P >= queue[0]:
                P -= queue.popleft()  # Buy the cheapest
                cur += 1
            else:
                P += queue.pop()  # Sell the most expensive
                cur -= 1
            res = max(res, cur)
        return res