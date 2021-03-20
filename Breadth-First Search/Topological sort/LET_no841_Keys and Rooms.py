class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = collections.deque([0])
        visited = {0}
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for room in rooms[cur]:
                    if room not in visited:
                        queue.append(room)
                        visited.add(room)
        
        return len(visited) == len(rooms)