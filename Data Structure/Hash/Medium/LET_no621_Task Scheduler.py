class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        memo = collections.Counter(tasks)
        max_freq = max(memo.values())
        res = (max_freq - 1) * (n + 1)
        
        for f in memo.values():
            if f == max_freq:
                res += 1
        
        return max(len(tasks), res)

        """
        example 1: memo = {'A':3, 'B':3}, n = 2
        prepare: A X X A X X 
        roop 1: A X X A X X A
        roop 2: A B X A B X A B

        example 2: memo = {'A':6, 'B':1, 'C':1, 'D':1, 'E':1, 'F':1, 'G':1}, n = 2 
        prepare: A X X A X X A X X A X X A X X
        roop 1: A X X A X X A X X A X X A X X A
        roop 2 - 7: A B C A D E A F G A X X A X X A
        """ 