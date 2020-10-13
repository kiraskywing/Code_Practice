class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        queue = collections.deque([id])
        video_freq = collections.defaultdict(int)
        friend_set = set()
        visited = [False] * len(friends)
        visited[id] = True

        for _ in range(level):
            for _ in range(len(queue)):
                id2 = queue.popleft()
                for id3 in friends[id2]:
                    if not visited[id3]:
                        queue.append(id3)
                        visited[id3] = True

        while queue:
            friend = queue.popleft()
            friend_set.add(friend)

        for friend in friend_set:
            for mov in watchedVideos[friend]:
                video_freq[mov] += 1

        ans = [key for key, value in sorted(video_freq.items(), key=lambda x: (x[1], x[0]))]
        return ans