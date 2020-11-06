class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if not pages:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_workers(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.get_workers(pages, start) <= k:
            return start
        return end

    def get_workers(self, books, time_limit):
        count, time = 0, 0
        for page in books:
            if time + page > time_limit:
                count += 1
                time = 0
            time += page
        return count + 1
