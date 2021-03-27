class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        record = collections.defaultdict(int)
        for s in B:
            for c in s:
                count = s.count(c)
                if count > record[c]:
                    record[c] = count
        
        sub_A = set(A)
        for s in A:
            for c in record:
                if s.count(c) < record[c]:
                    sub_A.remove(s)
                    break
        
        return list(sub_A)