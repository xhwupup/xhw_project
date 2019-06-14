# 时间：20190427
# Example:
#Example 1:
#Input: "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
# 难度：Medium(0.5)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s== None or len(s) ==0:
            return 0
        max_len = 0 #最大的字符串长度
        position={} #保存非重复字符最后的位置
        start=0     #保存非重复字符穿开始的位置
        for i in range(len(s)):
            if s[i] in position and position[s[i]] >= start:
                start = position[s[i]]+1
                position[s[i]] = i
            position[s[i]] = i
            current_len=i-start+1
            max_len=max(max_len,current_len)
        return max_len