class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # corner case: ["abc", "ab"], "abc" should be after "ab"
        
        # Approach: topological sorting
        # step1: build graph 
        #        => record how many chars are before a selected char (indegrees)
        #        => record the chars after a selected char (directed to)
        # step2: * put chars without any char before them (indegrees = 0) into queue
        #        * pop the front of queue. put the char to the list for output
        #        * get the next chars and subtract their indegrees by 1
        #        * if indegrees = 0, put the char into queue
        #        * repeat this step until no valid next char
        # step3: if all chars are used, return the result string. Otherwise empty string.
        
        cur_to_next = dict()    # Space: O(E), min: V - 1, max V ^ 2
        chars_before_cur = dict()    # Space: O(V) where V is the number of unique chars
        for w in words:
            for c in w:
                if c not in cur_to_next:
                    cur_to_next[c] = set()
                    chars_before_cur[c] = 0
                    
        for i in range(1, len(words)):    # Time: O(C) where C is the total chars iof input
            w1, w2 = words[i - 1], words[i]
            cond = len(w1) > len(w2)
            n = min(len(w1), len(w2))
            for j in range(n):
                a, b = w1[j], w2[j]
                if a != b:
                    if b not in cur_to_next[a]:
                        cur_to_next[a].add(b)
                        chars_before_cur[b] += 1
                    break
                elif j == n - 1 and cond:    # corner case
                    return ""
        
        res = []
        queue = collections.deque()
        for c, val in chars_before_cur.items():
            if val == 0:
                queue.append(c)
            
        while queue:    # Time: O(V + E)
            cur = queue.popleft()
            res.append(cur)
            for nxt in cur_to_next[cur]:
                chars_before_cur[nxt] -= 1
                if chars_before_cur[nxt] == 0:
                    queue.append(nxt)
        
        return ''.join(res) if len(res) == len(chars_before_cur) else ""