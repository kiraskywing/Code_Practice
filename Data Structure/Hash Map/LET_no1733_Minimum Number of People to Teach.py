class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        dontspeak = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if languages[u] & languages[v]:
                continue
            dontspeak.add(u)
            dontspeak.add(v)
        
        langcount = defaultdict(int)
        for p in dontspeak:
            for l in languages[p]:
                langcount[l] += 1
        
        return 0 if not dontspeak else len(dontspeak) - max(langcount.values())