"""
Begin by sorting the array to allow for efficient search of quadrulets.

The outer most forloop iterates for the first element of the quadruplet up
to n-3, allowing space for the other three elements. The second forloop iterates
for the second element of the quadruplet up to n-2, for the same reason. After that,
the two-pointer technique is used to find the last two elements.
"""


def fourSum(nums, target):
    nums.sort()  # Sort the array to handle duplicates and enable two-pointer technique
    n = len(nums)
    result = []

    # Iterate over first two elements
    for i in range(n - 3):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # Skip duplicates for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Use two pointers for the remaining two elements
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    # Add quadruplet to result
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:  # current_sum > target
                    right -= 1

    return result
