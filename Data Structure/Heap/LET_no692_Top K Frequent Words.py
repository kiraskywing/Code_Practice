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

"""Approach 2"""

class Node:
    def __init__(self, freq, word):
        self.freq, self.word = freq, word
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memo = collections.Counter(words)
        arr = [Node(freq, word) for word, freq in memo.items()]
        self.quickSelect(arr, 0, len(arr) - 1, k - 1)
        return [node.word for node in sorted(arr[:k], reverse=True)]
    
    def quickSelect(self, arr, left, right, target):
        if left >= right:
            return
        
        i, j = left, right
        pivot = arr[random.randint(left, right)]
        while i <= j:
            while i <= j and arr[i] > pivot:
                i += 1
            while i <= j and arr[j] < pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        if target <= j:
            self.quickSelect(arr, left, j, target)
        elif i <= target:
            self.quickSelect(arr, i, right, target)