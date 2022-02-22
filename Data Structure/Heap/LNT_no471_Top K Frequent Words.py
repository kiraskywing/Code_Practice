# The same as LeetCode no692. Top K Frequent Words

class Node:
    def __init__(self, s, count):
        self.s = s
        self.count = count
    def __lt__(self, other):
        if self.count == other.count:
            return self.s > other.s
        return self.count < other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memo = collections.Counter(words)
        temp = []
        for w, count in memo.items():
            heapq.heappush(temp, Node(w, count))
            if len(temp) > k:
                heapq.heappop(temp)
        
        res = []
        while temp:
            cur = heapq.heappop(temp)
            res.append(cur.s)
        return res[::-1]