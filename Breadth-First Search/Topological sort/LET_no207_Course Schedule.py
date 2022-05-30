class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        to_next_course = collections.defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            to_next_course[b].append(a)
            
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            cur = queue.popleft()
            numCourses -= 1
            for nxt in to_next_course[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return numCourses == 0