class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):

        next_courses = {index: [] for index in range(numCourses)}
        pre_times = [0 for _ in range(numCourses)]

        for course, pre_course in prerequisites:
            next_courses[pre_course].append(course)
            pre_times[course] += 1

        queue, count = collections.deque([]), 0

        for course in range(numCourses):
            if pre_times[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            count += 1

            for next_course in next_courses[course]:
                pre_times[next_course] -= 1
                if pre_times[next_course] == 0:
                    queue.append(next_course)

        return count == numCourses