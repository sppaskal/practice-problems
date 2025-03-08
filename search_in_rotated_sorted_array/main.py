class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1

        left, right = (0, len(nums) - 1)

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # if left is sorted
            if nums[left] <= nums[mid]:
                # if target within left side --> go left
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # if target within right side --> go right
                else:
                    left = mid + 1

            # if right is sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
