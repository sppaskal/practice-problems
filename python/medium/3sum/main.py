def threeSum(self, nums):
    """
    Finds all unique triplets in the array that sum to zero.
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums.sort()  # Sort the array to make it easier to skip duplicates and use two pointers
    result = []  # This will store the final list of triplets
    n = len(nums)

    # Loop through each number in the array
    for i in range(n):
        # Skip duplicate values for the first number to avoid repeating triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]  # We're looking for two numbers that sum to -nums[i]
        left, right = i + 1, n - 1  # Set up two pointers to scan the rest of the array

        # Use two pointers to find pairs that sum to the target
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicate values for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward to look for new pairs
                left += 1
                right -= 1

            elif current_sum < target:
                # If the sum is too small, move the left pointer to increase it
                left += 1
            else:
                # If the sum is too big, move the right pointer to decrease it
                right -= 1

    return result  # Return all found triplets
