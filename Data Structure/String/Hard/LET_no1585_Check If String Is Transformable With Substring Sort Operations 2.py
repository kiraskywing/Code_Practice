class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        places = collections.defaultdict(list)
        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)
        
        for e in t:
            key = int(e)
            if not places[key]:
                return False
            i = places[key][-1]
            for j in range(key):
                if places[j] and places[j][-1] < i:
                    return False
            places[key].pop()
        
        return True