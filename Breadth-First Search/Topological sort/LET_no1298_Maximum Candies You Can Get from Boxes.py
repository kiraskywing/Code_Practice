class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        queue = collections.deque(initialBoxes)
        visited = set()
        result = 0

        while queue:
            length, opened = len(queue), False
            while length > 0:
                box = queue.popleft()
                length -= 1
                if status[box] == 1:
                    opened = True
                    for key in keys[box]:
                        status[key] = 1
                    for next_box in containedBoxes[box]:
                        queue.append(next_box)
                    result += candies[box]
                else:
                    queue.append(box)
            if not opened:
                return result

        return result