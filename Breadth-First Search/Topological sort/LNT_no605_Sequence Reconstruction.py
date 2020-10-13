class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):

        graph = self.build_graph(seqs)
        topo_order = self.topo_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):

        graph = {}
        for seq in seqs:
            for elem in seq:
                if elem not in graph:
                    graph[elem] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def get_pretimes(self, graph):

        pretimes = {elem: 0 for elem in graph}

        for elem in graph:
            for nxt_elem in graph[elem]:
                pretimes[nxt_elem] += 1

        return pretimes

    def topo_sort(self, graph):
        pretimes = self.get_pretimes(graph)

        queue = []

        for elem in graph:
            if pretimes[elem] == 0:
                queue.append(elem)

        topo_order = []

        while queue:
            if len(queue) > 1:
                return None

            elem = queue.pop()
            topo_order.append(elem)

            for nxt_elem in graph[elem]:
                pretimes[nxt_elem] -= 1
                if pretimes[nxt_elem] == 0:
                    queue.append(nxt_elem)

        if len(topo_order) == len(graph):
            return topo_order

        return None