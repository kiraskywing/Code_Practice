class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            ID, condition, time = log.split(':')
            ID = int(ID)
            time = int(time)
            if condition == "start":
                if stack:
                    times[stack[-1]] += time - prev_time
                stack.append(ID)
                prev_time = time
            else:
                times[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        
        return times