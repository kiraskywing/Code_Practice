class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = cur = 0
        for arr, time in customers:
            cur = max(cur, arr) + time
            wait += cur - arr

        return wait / len(customers)