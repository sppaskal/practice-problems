class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # key == compliment, value == index
        compliments = {}

        for i, num in enumerate(nums):
            if num in compliments:
                return [compliments[num], i]

            # if compliment not found -->
            # add compliment of cur num
            compliment = target - num
            compliments[compliment] = i

        return []
