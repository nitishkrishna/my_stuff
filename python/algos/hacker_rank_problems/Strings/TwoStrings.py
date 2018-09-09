# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d_char = [0]*26
    for char in s1:
        d_char[ord(char)-ord('a')] +=1
    for char in s2:
        if d_char[ord(char)-ord('a')] > 0:
            return "YES"
    return "NO"

