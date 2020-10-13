class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        memo = collections.defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            memo[key].append(string)

        result = []
        for key in memo:
            if len(memo[key]) > 1:
                result.extend(memo[key])
        return result
