import collections

def get_shortest_unique_substring(arr, string):

  # left, right => [0, len(str) - 1]
  # hashmap, (key, value) = char, count
  
  # left = 0, right = 3 => {'x':1, 'y':2, 'z':1}
  # update right => 
  # left = 0, right = 4 => {'x':1, 'y':3, 'z':1}
  memo = collections.defaultdict(int)
  arr = set(arr)
  n = len(arr)
  
  res_left = 0
  res_right = len(string)
  
  left = 0

  for right in range(len(string)):
    if string[right] in arr:
      memo[string[right]] += 1
      n -= memo[string[right]] == 1
      
      if n == 0:
        while left <= right and (string[left] not in arr or memo[string[left]] > 1):
          memo[string[left]] -= 1
          left += 1

        if res_right - res_left > right - left:
          res_left, res_right = left, right
  
  if res_right - res_left == len(string):
    return ""
  
  return string[res_left:res_right+1]


arr = ['x','y','z']
string = "xyyzyzasddayx"