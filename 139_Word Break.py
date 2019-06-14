# 时间：20190524
# Example1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# 难度：Medium(0.5)



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0 or not wordDict:
            return False
        max_stride = max([len(x) for x in wordDict])
        res = [0] * (len(s) + 1)
        res[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(i-max_stride, i):
                if res[j] == 1 and s[j:i] in wordDict:
                    res[i] = 1
        if res[-1] == 1:
            return True
        else:
            return False
