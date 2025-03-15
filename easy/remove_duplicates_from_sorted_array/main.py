"""
Iterate through the array starting at index 1
so that you can compare to the previous index
right away, and use j as a way to keep track of
any duplicate values. This is achieved by not
incrementing j whenever a duplicate is encountered,
thus allowing us to replace the duplicate in the
next iteration that has a non duplicate value.
"""


def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
