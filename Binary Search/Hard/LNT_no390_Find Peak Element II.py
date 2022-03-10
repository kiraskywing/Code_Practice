class Solution:
	"""
	@param A: An integer matrix
	@return: The index of the peak
	"""
	def findPeakII(self, A):
		r_low, r_high = 0, len(A) - 1
		while r_low + 1 < r_high:
			r_mid = (r_low + r_high) // 2
			c = self.findMaxCol(A[r_mid])
			if A[r_mid][c] < A[r_mid - 1][c]:
				r_high = r_mid
			elif A[r_mid][c] < A[r_mid + 1][c]:
				r_low = r_mid
			else:
				return [r_mid, c]
		
		c1 = self.findMaxCol(A[r_low])
		c2 = self.findMaxCol(A[r_high])
		if A[r_low][c1] > A[r_high][c2]:
			return [r_low, c1]
		return [r_high, c2]

	def findMaxCol(self, nums):
		left, right = 0, len(nums) - 1
		while left + 1 < right:
			mid = (left + right) // 2
			if nums[mid] < nums[mid + 1]:
				left = mid
			else:
				right = mid

		if nums[left] > nums[right]:
			return left
		return right