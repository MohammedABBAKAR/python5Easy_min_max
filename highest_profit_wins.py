# Write a function that returns both the minimum and maximum number 
# of the given list/array.

# Examples (Input --> Output)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]

def min_max(lst):
    if not lst:
        return []
    
    arr2 = []
    x = max(lst)
    y = min(lst)
    arr2.append(x)
    arr2.append(y)
    return arr2

print(min_max([1, 2, 3, 4, 5]))
