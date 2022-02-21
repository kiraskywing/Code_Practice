# The same as LeetCode no1086. High Five

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        Hash = collections.defaultdict(list)

        for student in results:
            heapq.heappush(Hash[student.id], student.score)
            if len(Hash[student.id]) > 5:
                heapq.heappop(Hash[student.id])

        ans = dict()
        for ID, scores in Hash.items():
            ans[ID] = sum(scores) / 5
        return ans