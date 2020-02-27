# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : easy3.py
# @Time     : 2020.02.26

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Q21 合并两个有序链表 d200227
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)  # 头结点
        l = ans
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
                l = l.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
                l = l.next
        if l1:
            l.next = l1
        if l2:
            l.next = l2
        return ans.next

    # Q88 合并两个有序数组 直接合并后排序 O((n+m)lg(n+m))  从后往前排序 O(n+m) d200227
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = n + m - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        # [3,0] 1 [2] 1 可能i先<0 要把nums2没比完的部分移上来 但j<0时不需要动
        nums1[: j + 1] = nums2[: j + 1]

    # Q977 有序数组的平方 平方后排序O(nlgn)  240 ms  合并两有序数组 O(n)  268 ms  d200227
    def sortedSquares(self, A: List[int]) -> List[int]:
        # A列表分成两段 A1 [-7 -3] B1 [2, 3, 11]
        l = len(A)
        j = 0
        while j < l and A[j] < 0:
            j += 1  # 非负数最小
        i = j - 1  # 负数最大
        ans = []
        while i >= 0 and j < l:
            if A[i] * A[i] <= A[j] * A[j]:
                ans.append(A[i] * A[i])
                i -= 1
            else:
                ans.append(A[j] * A[j])
                j += 1
        if i >= 0:
            ans = ans + [A[k] * A[k] for k in range(i, -1, -1)]
        else:
            ans = ans + [A[k] * A[k] for k in range(j, l, 1)]
        return ans




if __name__ == "__main__":
    s = Solution()
    # a1 = ListNode(1)
    # a2 = ListNode(2)
    # a3 = ListNode(4)
    # b1 = ListNode(1)
    # b2 = ListNode(3)
    # b3 = ListNode(4)
    # a1.next = a2
    # a2.next = a3
    # b1.next = b2
    # b2.next = b3
    # ans = s.mergeTwoLists(a1, b1)
    # while ans:
    #     print(ans.val, end=" ")
    #     ans = ans.next

    # Q88
    # nums1 = [3,0]
    # nums2 = [2]
    # s.merge(nums1, 1, nums2, 1)
    # print(nums1)

    print(s.sortedSquares([-7, -3, 2, 3, 11]))
