import heapq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        memo = collections.defaultdict(int)
        for word in words:
            memo[word] += 1

        maxheap = []
        for word in memo:
            heapq.heappush(maxheap, (-memo[word], word))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(maxheap)[1])

        return result
