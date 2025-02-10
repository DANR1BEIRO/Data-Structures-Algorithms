def binary_search(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return "Target isn't in array"


def exponential_search(array, target):
    if array[0] == target:
        return 0
    n = len(array)
    right = 1
    
    while right < n and array[right] < target:
        right *= 2
        
    if array[right] == target:
        return right

    return binary_search(array, target, right//2, min(right,n-1))

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 7
result = exponential_search(array, target)

print(f"Target found at index {result}")
    
    