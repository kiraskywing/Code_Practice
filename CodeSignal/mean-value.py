import collections

def solution(arr):
    memo = collections.defaultdict(list)

    for i, row in enumerate(arr):
        val = sum(row) / len(row)
        memo[val].append(i)
    
    return [vals for vals in memo.values()]