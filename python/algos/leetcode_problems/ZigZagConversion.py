"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_len = len(s)
        s_count = 0
        row_strs = list()
        for x in range(numRows):
            row_strs.append("")
        while s_count<s_len:
            for x in range(0,numRows):
                if s_count<s_len:
                    row_strs[x]+=(s[s_count])
                    s_count+=1
                else:
                    break
            for y in range(numRows-2,0,-1):
                if s_count<s_len:
                    row_strs[y]+=(s[s_count])
                    s_count+=1
                else:
                    break
        ret_str=""
        for x in range(numRows):
            ret_str+=str(row_strs[x])

        return ret_str
