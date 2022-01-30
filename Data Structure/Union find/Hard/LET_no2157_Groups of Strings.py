class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        px, py = self.find(self.root[x]), self.find(self.root[y])
        if px != py:
            self.root[py] = px

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        mask2word = {sum(1 << (ord(c) - ord('a')) for c in w) : idx for idx, w in enumerate(words)}
        subMask2word = collections.defaultdict(list)
        n = len(words)
        uf = UnionFind(n)
        
        for idx, w in enumerate(words):
            mask = 0
            vals = []
            for c in w:
                val = ord(c) - ord('a')
                mask += 1 << val
                vals.append(val)
                
            for val in vals:
                replaced = mask - (1 << val) + 1 << 26    # 1 << 26 denotes replacing one letter
                subMask2word[replaced].append(idx)
                deleted = mask - (1 << val)    # delete one letter
                if deleted not in mask2word:
                    continue
                idx2 = mask2word[deleted]
                uf.union(idx, idx2)
        
        for group in subMask2word.values():
            for a, b in zip(group, group[1:]):
                uf.union(a, b)
        
        for i in range(n):
            uf.find(i)    # update all parents
        counts = collections.Counter(uf.root)
        return [len(counts), max(counts.values())]