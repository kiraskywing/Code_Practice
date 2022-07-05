class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.email_to_id = dict()
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, email):
        if email not in self.email_to_id:
            self.email_to_id[email] = i
            return
        
        j = self.email_to_id[email]
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.parent[pi] = pj

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(1, len(accounts[i])):
                uf.union(i, accounts[i][j])
        
        id_to_email = collections.defaultdict(list)
        for email, i in uf.email_to_id.items():
            p = uf.find(i)
            id_to_email[p].append(email)
            
        res = []
        for i, emails in id_to_email.items():
            temp = [accounts[i][0]]
            temp.extend(sorted(emails))
            res.append(temp)
        
        return res