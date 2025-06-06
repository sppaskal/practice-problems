def longestPalindrome(self, s: str) -> str:

    # Checks to see if current char is the right-most index of a
    # palindrome in the parent string.
    def look_for_pal(cur_char_indices, left_index, right_index):
        sub_string = s[cur_char_indices[left_index]:cur_char_indices[right_index] + 1]
        # if sub string is palindrome then return the index range
        if sub_string == sub_string[::-1]:
            return cur_char_indices[left_index], cur_char_indices[right_index]
        # if sub string is not a palindrome and another closer left_index
        # exists --> attempt to see if that is a palindrome relative to right_index
        elif left_index + 1 < len(cur_char_indices) - 1:
            return look_for_pal(cur_char_indices, left_index + 1, right_index)
        # if sub string is not palindrome and there are no other left indices to check
        # then the current char is not the right-most index of a palindrome.
        else:
            return None, None

    visited_chars = {}
    longest_pal = s[0]
    for i in range(len(s)):
        if s[i] not in visited_chars.keys():
            visited_chars[s[i]] = [i]
        else:
            visited_chars[s[i]].append(i)
            cur_char_indices = visited_chars.get(s[i])
            l_index, r_index = look_for_pal(
                cur_char_indices=cur_char_indices,
                left_index=0,
                right_index=-1
            )

            if l_index is not None and r_index is not None:
                cur_pal = s[l_index:r_index + 1]
                if len(cur_pal) > len(longest_pal):
                    longest_pal = cur_pal

    return longest_pal
