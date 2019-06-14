#时间：20190503
#Example1:
#Input: "()"
#Output: true
#Example2:
#Input: "()[]{}"
#Output: true
#Example3:
#Input: "(]"
#Output: false
#Example4:
#Input: "([)]"
#Output: false
#难度：Easy(0.5)
class Solution:
    def isValid(self, s: str) -> bool:
        a = {')':'(', ']':'[', '}':'{'}  #右括号对应最括号的字典
        l = [None]  #设置None排除空值的情况
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()  #右括号, 且与最后一个最括号对应, 出栈
            else:
                l.append(i)  #左括号入栈
        return len(l)==1