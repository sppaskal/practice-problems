def lengthOfLastWord(self, s):
    s = s.strip()  # remove leading/trailing spaces
    words = s.split(' ')  # split s into words

    if not words:
        return None

    return len(words[-1])  # return length of last word
