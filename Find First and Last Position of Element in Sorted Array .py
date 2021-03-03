nums = [5, 7, 7, 8, 8, 10]
target = 8


def first_occurence(nums, target):
    left, right = 0, len(nums)-1
    res = -1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            res = mid
            right = mid-1
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return res


def last_occurence(nums, target):
    left, right = 0, len(nums)-1
    res = -1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            res = mid
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return res


print([first_occurence(nums, target), last_occurence(nums, target)])
