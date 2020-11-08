class Solution:
    """
    @param str: A string
    @return: A string
    """
    def lowercaseToUppercase2(self, str):

        res = ''
        for i in str:
            if ord("a") <= ord(i) and ord(i) <= ord("z"):
                res += chr(ord("A") + (ord(i) - ord("a")))
            else:
                res += i

        return res

if __name__ == '__main__':
    ans = Solution()
    print(ans.lowercaseToUppercase2("abc"))