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

            # if num is a compliment to any previous num
            # --> return both of their indices
            if num in compliments:
                return [compliments[num], i]

            # if cur num is not a compliment to a previous num
            # --> add compliment of cur num to compliments dict
            compliment = target - num
            compliments[compliment] = i

        return []
