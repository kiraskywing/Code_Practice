# The same as LeetCode no210. Course Schedule II

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):

        pre_to_nxts = {i: [] for i in range(numCourses)}
        pre_times = [0 for _ in range(numCourses)]

        for nxt, pre in prerequisites:
            pre_to_nxts[pre].append(nxt)
            pre_times[nxt] += 1

        queue, result = collections.deque([]), []

        for course in range(numCourses):
            if pre_times[course] == 0:
                queue.append(course)

        while queue:
            pre = queue.popleft()
            result.append(pre)

            for nxt in pre_to_nxts[pre]:
                pre_times[nxt] -= 1
                if pre_times[nxt] == 0:
                    queue.append(nxt)

        if len(result) == numCourses:
            return result

        return []