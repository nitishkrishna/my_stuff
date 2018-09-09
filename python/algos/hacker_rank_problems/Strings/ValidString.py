def isValid(s):
    chars = dict()
    for ch in s:
        chars[ch] = chars.get(ch, 0) + 1
    vals = list(chars.values())
    counts = dict()
    for val in vals:
        counts[val] = counts.get(val,0) + 1
    # more than 2 chars
    print counts
    if len(counts) > 2:
        return 'NO'
    # only 1 char or out of 2 differing chars one has count == 1
    elif len(counts) == 1:
        return 'YES'
    elif min(counts.values()) == 1:
        if abs(counts.keys()[0]-counts.keys()[1])==1:
            return 'YES'
        elif 1 in counts and counts[1] == 1:
            return 'YES'
        else:
            return 'NO'
    # other cases
    return 'NO'

