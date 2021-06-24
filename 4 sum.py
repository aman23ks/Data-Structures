# def fourSum(nums, target):
#     nums = sorted(nums)
#     hashmap = {}
#     values = []
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j] not in hashmap:
#                 hashmap[nums[i]+nums[j]] = [(i, j)]
#             else:
#                 hashmap[nums[i]+nums[j]].append((i, j))

#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             sum = target - (nums[i]+nums[j])
#             if sum in hashmap:
#                 for ele in hashmap[sum]:
#                     k = ele[0]
#                     l = ele[1]
#                     if k>j:

#     print(hashmap)


# fourSum([1, 0, -1, 0, -2, 2], 0)
