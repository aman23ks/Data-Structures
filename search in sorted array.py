nums = [4, 5, 6, 7, 0, 1, 2, 3]
target = 0


class Solution:

    def search(self):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
