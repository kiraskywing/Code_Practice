def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort(reverse=True)
    grantsArray.append(0)
    surplus = sum(grantsArray) - newBudget

    if surplus <= 0:
        return grantsArray[0]
        
    i = 0
    while i < len(grantsArray) - 1:
        surplus -= (i + 1) * (grantsArray[i] - grantsArray[i + 1])
        if surplus <= 0:
            break
        i += 1
        
    return grantsArray[i + 1] + (float(-surplus) / (i + 1))

def find_grants_cap2(arr, budget):
    left, right = 0, max(arr)
    
    while right - left >= 1e-10:
        mid = (left + right) / 2.0
        total = sum(min(num, mid) for num in arr)
        if total >= budget:
            right = mid
        elif total < budget:
            left = mid

    if sum(min(num, left) for num in arr) <= budget:
        return round(left, 8)
    return round(right, 8)
  
grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))
  
grantsArray = [2, 4]
newBudget = 3
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))

grantsArray = [2, 4, 6]
newBudget = 3
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))
  
grantsArray = [2,100,50,120,167]
newBudget = 400
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))

grantsArray = [2,100,50,120,1000]
newBudget = 190
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))

grantsArray = [21,100,50,120,130,110]
newBudget = 140
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))

grantsArray = [210,200,150,193,130,110,209,342,117]
newBudget = 1530
print(find_grants_cap(grantsArray, newBudget), find_grants_cap2(grantsArray, newBudget))