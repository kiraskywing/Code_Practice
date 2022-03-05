class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        email_id = dict()
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in email_id:
                    self.union(parent, i, email_id[email])
                else:
                    email_id[email] = i
        
        mres = collections.defaultdict(list)
        for email, i in email_id.items():
            p = self.find(parent, i)
            mres[p].append(email)
            
        res = []
        for key, values in mres.items():
            temp = [accounts[key][0]]
            temp.extend(sorted(values))
            res.append(temp)
        return res
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, i, j):
        pi, pj = self.find(parent, i), self.find(parent, j)
        if pi != pj:
            parent[pj] = pi