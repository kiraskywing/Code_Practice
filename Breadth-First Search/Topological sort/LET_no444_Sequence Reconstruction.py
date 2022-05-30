class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        indegree = [0] * n
        graph = collections.defaultdict(list)
        self.buildGraph(sequences, indegree, graph)
        
        queue = collections.deque([i for i in range(n) if indegree[i] == 0])
        i = 0
        while queue:
            if len(queue) > 1:
                return False
            
            cur = queue.popleft()
            if cur + 1 != nums[i]:
                return False
            i += 1
            
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
            
        return True
    
    def buildGraph(self, seqs, indegree, graph):
        for seq in seqs:
            for i in range(1, len(seq)):
                a, b = seq[i - 1] - 1, seq[i] - 1
                graph[a].append(b)
                indegree[b] += 1