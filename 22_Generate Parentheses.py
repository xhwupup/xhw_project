#时间：20190503
#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]
#难度：Medium（0.5）

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        :type n: int
        :rtype: List[str]
        """
        self.res= []
        self.generateParenthesisIter('',n,n)
        return self.res
    def generateParenthesisIter(self,mstr,r,l):
        if r==0 and l==0:
            self.res.append(mstr)
            #如果左括号的个数还有剩余，则+’(‘然后递归
        if l>0:
            self.generateParenthesisIter(mstr+'(',r,l-1)
            #如果右括号有剩余且小于左括号的个数则+‘）’
        if r>0 and r>l:
            self.generateParenthesisIter(mstr+')',r-1,l)