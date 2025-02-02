def binary_search(nums, target):

    left, right = 0, len(nums) -1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if nums[mid] == target:
            print(f"Steps: {steps}")
            return mid
        
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

a = [1, 2, 3, 4, 5]
b = a + [6, 7, 8, 9, 10]
c = b + [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = c + [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

binary_search(a, 5)
binary_search(b, 5)
binary_search(c, 5)
binary_search(d, 5)
# [1, 2, 3, 4, 5]