# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : middle2.py
# @Time     : 2020.02.26

# 两个单链表相加


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Q2 两数相加 低位-高位 d200226
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = l1.val + l2.val
        ans = ListNode(value % 10)
        n = value // 10
        l = ans
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            value = l1.val + l2.val + n
            l.next = ListNode(value % 10)
            n = value // 10
            l = l.next
        while l1.next:
            l1 = l1.next
            value = l1.val + n
            l.next = ListNode(value % 10)
            n = value // 10
            l = l.next
        while l2.next:
            l2 = l2.next
            value = l2.val + n
            l.next = ListNode(value % 10)
            n = value // 10
            l = l.next
        if n > 0:
            l.next = ListNode(1)
        return ans

    # Q445 两数相加II 高位-低位 无法倒转 用栈 先进后出 d200226
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1 = []
        stack_2 = []
        ans = []
        n = 0
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next
        while stack_1 and stack_2:
            value = stack_1.pop() + stack_2.pop() + n
            ans.append(value % 10)
            n = value // 10
        while stack_1:
            value = stack_1.pop() + n
            ans.append(value % 10)
            n = value // 10
        while stack_2:
            value = stack_2.pop() + n
            ans.append(value % 10)
            n = value // 10
        if n > 0:
            ans.append(n)
        h = ListNode(ans.pop())
        l = h
        while ans:
            l.next = ListNode(ans.pop())
            l = l.next
        return h


if __name__ == "__main__":
    s = Solution()
    # a1 = ListNode(2)
    # a2 = ListNode(4)
    # a3 = ListNode(3)
    # b1 = ListNode(5)
    # b2 = ListNode(6)
    # b3 = ListNode(4)
    # a1.next = a2
    # a2.next = a3
    # b1.next = b2
    # b2.next = b3
    # ans = s.addTwoNumbers(a1, b1)
    # while ans:
    #     print(ans.val, end=" ")
    #     ans = ans.next
    a1 = ListNode(7)
    a2 = ListNode(2)
    a3 = ListNode(4)
    a4 = ListNode(3)
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(4)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    b1.next = b2
    b2.next = b3
    ans = s.addTwoNumbers2(a1, b1)
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
