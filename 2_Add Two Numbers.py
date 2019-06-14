# 时间：20190427
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 80
# 难度：Medium(0.5)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        tmp=ListNode(0) #引用ListNode类定义了一个链表节点并赋值，tmp是暂存，temporal
        res=tmp         #res是重置，reset
        flag=0          #flag是标识 初始化
        while l1 or l2: #l1或l2不为空就继续执行
            tmp_sum=0   #链表节点值的和
            if l1:      #如果l1不为空，把l1的某个节点的值赋给tmp_sum
                tmp_sum=l1.val  #把l1的某个节点的值赋给tmp_sum
                l1=l1.next
            if l2:      #如果l2不为空，把l1和l2对应的节点的值赋给tmp_sum
                tmp_sum+=l2.val
                l2=l2.next  #指向下一个节点。为下次的加和做准备
            tmp_res=((tmp_sum+flag)%10) #个位数字
            flag = ((tmp_sum+flag)//10) #进位的数
            res.next=ListNode(tmp_res)
            res=res.next    #res后移
            if flag:    #如果flag不为0，就是对应位置相加后有进位
                res.next=ListNode(1)    #res的下一个节点为1
        res=tmp.next    #赋值
        del tmp         #删除tmp变量
        return res      #返回res链表
