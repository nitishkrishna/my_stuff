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