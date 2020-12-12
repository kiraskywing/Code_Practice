class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        to_childs = {i: set() for i in range(nodes)}
        for child, father in enumerate(parent):
            if child > 0:
                to_childs[father].add(child)

        total_sum, total_count = self.dfs(0, value, to_childs)
        return total_count

    def dfs(self, father, value, to_childs):
        total_sum, total_count = value[father], 1

        for child in to_childs[father]:
            child_sum, child_count = self.dfs(child, value, to_childs)
            if child_sum != 0:
                total_sum += child_sum
                total_count += child_count

        if total_sum != 0:
            return total_sum, total_count
        return 0, 0

    # Solution 2:
        count = [1] * nodes
        for child in range(nodes - 1, 0, -1):
            if value[child] != 0:
                value[parent[child]] += value[child]
                count[parent[child]] += count[child]
        return count[0]