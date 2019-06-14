# 时间：20190527
#
# 难度：Easy(0.25)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    //这个思路就是 ListA + ListB = A + intersection + Bb + intersection
    //             ListB + ListA = Bb + intersection + A + intersection
    //           用大A表示ListA里面非共有 Bb表示listB里面非共有的，可以看到在第二个intersection的开头两个链表长度是一样的，必然相等
    //           所以我们可以遍历A再遍历B，另一个遍历B再遍历A，两个指针必定在第二个交集处相遇，没有交集就是空指针
        ListNode *cursorA = headA;
        ListNode *cursorB = headB;
        if (!cursorA || !cursorB)
            return NULL;
        while (cursorA != cursorB)
        {
            if (!cursorA)
                cursorA = headB;
            else
                cursorA = cursorA->next;
            if (!cursorB)
                cursorB = headA;
            else
                cursorB = cursorB->next;
        }
        return cursorA;

    }
};