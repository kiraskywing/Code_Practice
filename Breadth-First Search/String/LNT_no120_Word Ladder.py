class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):

        dict.add(end)
        queue = collections.deque([start])
        visited = set(start)
        steps = 0

        while queue:
            steps += 1

            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return steps

                for next_word in self.get_next_words(word):
                    if next_word in dict and next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)

        return 0

    def get_next_words(self, word):
        words = []

        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                words.append(left + char + right)

        return words