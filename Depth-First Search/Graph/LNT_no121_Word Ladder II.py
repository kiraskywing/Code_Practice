# The same as LeetCode no126. Word Ladder II

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):

        dict.add(start)
        dict.add(end)
        distance = {}

        self.bfs(end, distance, dict)

        path, result = [start], []
        self.dfs(start, end, distance, dict, path, result)
        return result

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = collections.deque([start])

        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, dict):
        words = []

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if word[i] != c:
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in dict:
                        words.append(next_word)
        return words

    def dfs(self, cur, target, distance, dict, path, result):
        if cur == target:
            result.append(path[:])
            return

        for word in self.get_next_words(cur, dict):
            if distance[word] != distance[cur] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, result)
            path.pop()