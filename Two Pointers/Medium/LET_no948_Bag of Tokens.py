class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            else:
                if right - left > 1 and score > 0:
                    power += tokens[right]
                    score -= 1
                    right -= 1
                else:
                    break
        
        return score

class Solution2:
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