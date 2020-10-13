class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]

        for i in range(len(queries)):
            start, end = queries[i][0], queries[i][1]
            queries[i] = prefix[end + 1] ^ prefix[start]

        return queries