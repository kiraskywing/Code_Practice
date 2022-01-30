class Solution:
    """
    @param A: Integer array
    @param k: a integer
    @return: return is possible to partition the array satisfying the above conditions
    """
    def PartitioningArray(self, A, k):
        # write your code here
        if len(A) % k != 0:
            return False
        
        groups = len(A) // k
        record = collections.Counter(A)
        return all(n <= groups for n in record.values())