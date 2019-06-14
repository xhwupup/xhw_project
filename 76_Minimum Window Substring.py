# 时间:20190513
# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#     If there is no such window in S that covers all characters in T, return the empty string "".
#     If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
# 难度：Hard(1.0)

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        for c in t:
            mem[c] += 1
        t_len = len(t)
        minL, minR = 0, float('inf')
        l = 0
        for r, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1
            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1
                if r - l < minR - minL:
                    minL, minR = l, r
                mem[s[l]] += 1
                t_len += 1
                l += 1
        return '' if minR == float('inf') else s[minL:minR + 1]
