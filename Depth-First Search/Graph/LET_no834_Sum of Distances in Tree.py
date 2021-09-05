class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        trees = collections.defaultdict(set)
        for i, j in edges:
            trees[i].add(j)
            trees[j].add(i)
        res = [0] * n
        count = [1] * n
        
        def postOrder(root, pre):
            for i in trees[root]:
                if i != pre:
                    postOrder(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        
        def preOrder(root, pre):
            for i in trees[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    preOrder(i, root)
        
        postOrder(0, -1)
        preOrder(0, -1)
        
        return res