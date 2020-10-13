class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        res = []
        for num in range (1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                res.append("fizz buzz")
            elif num % 3 == 0:
                res.append("fizz")
            elif num % 5 == 0:
                res.append("buzz")
            else:
                res.append(str(num))
        return res

        """
        solution 2
        i, p3, p5 = 1, 1, 1
        res = []
        
        while i <= n:
            while i <= n and i < p3 * 3 and i < p5 * 5:
                res.append(str(i))
                i += 1
                
            if i <= n and p3 * 3 == p5 * 5 :
                res.append("fizz buzz")
                i += 1
                p3 += 1
                p5 += 1
            
            while i <= n and p3 * 3 <= i:
                res.append("fizz")
                i += 1
                p3 += 1
                
            while i <= n and p5 * 5 <= i:
                res.append("buzz")
                i += 1
                p5 += 1
            
        return res
        """

if __name__ == '__main__':
    res = Solution()
    print(res.fizzBuzz(10))