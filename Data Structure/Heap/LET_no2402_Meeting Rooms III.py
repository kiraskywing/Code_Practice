class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ready_rooms = [i for i in range(n)]
        heapq.heapify(ready_rooms)
        booked_rooms = []    # (end_time, room_id)
        used_times = [0 for _ in range(n)]

        for start_time, end_time in sorted(meetings):
            while booked_rooms and booked_rooms[0][0] <= start_time:
                _, room_id = heapq.heappop(booked_rooms)
                heapq.heappush(ready_rooms, room_id)
            
            room_id = None
            if ready_rooms:
                room_id = heapq.heappop(ready_rooms)
                heapq.heappush(booked_rooms, (end_time, room_id))
            else:
                prev_end_time, room_id = heapq.heappop(booked_rooms)
                heapq.heappush(booked_rooms, (prev_end_time + end_time - start_time, room_id))
            used_times[room_id] += 1
        
        return used_times.index(max(used_times))
