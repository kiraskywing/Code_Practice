import collections

def solution(queryType, query):
    res = 0
    memo = dict()
    
    extra_key = 0
    extra_value = 0

    for s, values in zip(queryType, query):
        if s == "insert":
            key, val = values
            memo[key-extra_key] = val - extra_value

        elif s == "addToKey":
            extra_key += values[0] 

        elif s == "addToValue":
            extra_value += values[0]

        else:
            res += memo[values[0]-extra_key] + extra_value

    return res

queryType = [
    "insert", "addToKey", "insert", "addToValue", "get", "get"
]

query = [
    [1, 1], [3], [2, 2], [4], [4], [2]
]

print(solution(queryType, query))