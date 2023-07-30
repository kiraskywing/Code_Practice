class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [ai, bi]: take bi before ai
        # numCourses = 0? => no
        
        # Approach: BFS
        # step.1 build graph, record the number of prereqs of each courses, set remains = numCourses
        # step.2 put courses with zero prereq into queue and output list, remains substract corresponding number
        # step.3 find next courses with zero prereq
        # step.4 repeat step2 and 3 until no next course
        # step.5 return output list if remain is 0 else empty list
        
        num_of_prereqs = [0] * numCourses    # Space: O(V)
        next_can_take = collections.defaultdict(list)    # Space: O(E)
        remain = numCourses
        res = []
        queue = collections.deque([])    # Space: O(V)
        
        for a, b in prerequisites:    # Time: O(E)
            num_of_prereqs[a] += 1
            next_can_take[b].append(a)
            
        for i in range(numCourses):    # Time: O(V)
            if num_of_prereqs[i] == 0:
                remain -= 1
                res.append(i)
                queue.append(i)
        
        while queue:    # Time: O(V+E)
            cur = queue.popleft()
            for nxt in next_can_take[cur]:
                num_of_prereqs[nxt] -= 1
                if num_of_prereqs[nxt] == 0:
                    remain -= 1
                    res.append(nxt)
                    queue.append(nxt)
        
        return res if remain == 0 else []