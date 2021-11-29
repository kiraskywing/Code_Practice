class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        email_id = dict()
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in email_id:
                    p1 = self.find(parent, i)
                    p2 = self.find(parent, email_id[email])
                    parent[p2] = p1
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