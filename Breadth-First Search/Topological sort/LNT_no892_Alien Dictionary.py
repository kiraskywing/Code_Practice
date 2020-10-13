import heapq


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        graph = self.build_graph(words)
        return self.topological_sort(graph)

    def build_graph(self, words):
        graph = dict()
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = []

        n = len(words)
        for i in range(1, n):
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i - 1][j] != words[i][j]:
                    graph[words[i - 1][j]].append(words[i][j])
                    break

        return graph

    def topological_sort(self, graph):
        indegree = {node: 0 for node in graph}

        for node in graph:
            for next_node in graph[node]:
                indegree[next_node] += 1

        queue = [node for node in graph if indegree[node] == 0]
        heapq.heapify(queue)
        result = []

        while queue:
            node = heapq.heappop(queue)
            result.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    heapq.heappush(queue, next_node)

        if len(result) == len(graph):
            return ''.join(result)

        return ''