# 时间：20190512
# Example1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# nention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 难度:Hard(1.0)
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_len, word2_len = len(word1), len(word2)
        mem = [[0]*(word2_len+1) for _ in range(word1_len+1)]
        for i in range(1, word1_len+1):
            mem[i][0] = i
        for j in range(1, word2_len+1):
            mem[0][j] = j

        for i in range(1, word1_len+1):
            for j in range(1, word2_len+1):
                mem[i][j] = min(mem[i-1][j-1]+(word1[i-1]!=word2[j-1]), mem[i][j-1]+1, mem[i-1][j]+1)

        return mem[-1][-1]
