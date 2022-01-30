class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_to_time = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = time.split(':')
            time2 = 60 * int(hour) + int(minute)
            name_to_time[name].append(time2)
        
        result = []
        for name, time_list in name_to_time.items():
            time_list.sort()
            left = 0
            for right, time in enumerate(time_list):
                while left < right and time - time_list[left] > 60:
                    left += 1
                if right - left >= 2 and time - time_list[left] <= 60:
                    result.append(name)
                    break
        
        return sorted(result)