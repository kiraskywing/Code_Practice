class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        que = collections.deque([s])
        hash = set([s])
        min_len = len(s)

        while que:
            string = que.popleft()
            for sub in dict:
                find_i = string.find(sub)
                while find_i != -1:
                    new_string = string[:find_i] + string[find_i + len(sub):]

                    if new_string not in hash:
                        if len(new_string) < min_len:
                            min_len = len(new_string)
                        que.append(new_string)
                        hash.add(new_string)

                    find_i = string.find(sub, find_i + 1)

        return min_len
