"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_sub_string_length = 0
        start_idx=0
        end_idx=0
        sub_dict = dict()
        cur_str = ""
        if len(s):
            for idx, val in enumerate(s):
                if str(val) not in cur_str:
                    sub_dict[str(val)] = idx
                    cur_str += str(val)
                    end_idx = idx
                else:
                    length = end_idx-start_idx+1
                    if length > longest_sub_string_length:
                        longest_sub_string_length = length
                    start_idx = sub_dict[str(val)]+1
                    end_idx = idx
                    sub_dict[str(val)] = idx
                    cur_str = s[start_idx:end_idx+1]
            length = end_idx-start_idx+1
            if length > longest_sub_string_length:
                longest_sub_string_length = length
        return longest_sub_string_length

# 23.88 percentile