def longest_unique_substring(s):
    seen = set()         # Tracks characters currently in the window
    left = 0             # Left boundary of the sliding window
    max_len = 0          # Tracks the maximum length found

    # Expand the window by moving the right pointer
    for right in range(len(s)):
        # If the character at 'right' is already in the window,
        # shrink the window from the left until it's removed
        while s[right] in seen:
            seen.remove(s[left])  # Remove the leftmost character
            left += 1             # Move the left boundary forward

        # Add the new character to the window
        seen.add(s[right])

        # Update the max length if this window is larger
        max_len = max(max_len, right - left + 1)

    return max_len
