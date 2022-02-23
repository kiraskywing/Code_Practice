from random import randint

class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        return cls(n, k)

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.used_points = set()
        self.machines = collections.defaultdict(list)

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        for _ in range(self.k):
            point = randint(0, self.n - 1)
            while point in self.used_points:
                point = randint(0, self.n - 1)
            self.used_points.add(point)
            self.machines[machine_id].append(point)
        
        self.machines[machine_id].sort()
        return self.machines[machine_id]

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        machine_id = -1
        distance = self.n + 1

        for mId, points in self.machines.items():
            closestP = self.binarySearch(points, hashcode)
            d = closestP - hashcode
            if d < 0:
                d += self.n
            if d < distance:
                distance = d
                machine_id = mId
        
        return machine_id

    def binarySearch(self, points, target):
        left, right = 0, len(points) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if points[mid] < target:
                left = mid
            else:
                right = mid
        if points[left] >= target:
            return points[left]
        if points[right] >= target:
            return points[right]
        return points[0]
