class Solution:
    """
    @param elements: A list of recommended elements.
    @param n: [picture P] can appear at most 1 in every n
    @return: Return the scattered result.
    """
    def scatter(self, elements, n):
        # write your code here
        first_p = False
        p = collections.deque([])
        v = collections.deque([])
        res = []
        for s in elements:
            if not first_p:
                if s[0] == 'P':
                    first_p = True
                    p.append(s)
                else:
                    res.append(s)
            else:
                if s[0] == 'P':
                    p.append(s)
                else:
                    v.append(s)
        
        for i in range(len(p) + len(v)):
            if i % n == 0 and p:
                res.append(p.popleft())
            elif i % n != 0 and v:
                res.append(v.popleft())
            else:
                break
        
        return res
