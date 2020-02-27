# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : middle3.py
# @Time     : 2020.02.26

# 滑动窗口
from typing import List


class Solution:
    # Q3 无重复字符的最长子串 暴力枚举O(n^3)  解法一：滑动窗口 O(2n) 最糟糕的情况下每个字符会被i和j访问两次 d200227
    # s[i][j-1]若无重复字符 那么s[i][j]是否有重复字符只需要判别s[j]对应的字符是否存在在字符串s[i][j-1]中就可以了
    # 使用hashset作为滑动窗口，来完成检查 O(1)  128 ms
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = len(s)
        i = 0  # 窗口两端[i,j) 当前判断s[j]
        j = 0
        w = set()  # 空间复杂度 O(min(l,m))  m为字符集大小 l为字符串长度
        while i < l and j < l:
            if s[j] not in w:  # 窗口里没有s[j]
                w.add(s[j])
                j += 1
                ans = max(ans, j-i)  # 窗口大小j-i
            else:  # 窗口有s[j],以s[i]开头的最长无重复字符不可能比此时的ans更大了，继续看i+1
                w.remove(s[i])
                i += 1
        return ans

    # Q3 无重复字符的最长子串 解法二：优化滑动窗口 O(n) 循环一遍j 用dic记录字符和索引 直接跳转到重复字符的位置 d200227
    # 例如 abcb j=3 "b"与j'=1的"b"重复 因为dic记录下了b的索引1，所以i直接跳转到j'+1即可  64 ms
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        ans = 0
        l = len(s)
        i = 0
        j = 0
        w = {}  # 字符:索引
        while j < l:
            if s[j] not in w or w[s[j]] < i:  # cbabcb 有些字符已经在字典中但是索引比i大 其实不在滑动窗口内 比如abc中的c
                w[s[j]] = j
                j += 1
                ans = max(ans, j-i)
            else:
                i = w[s[j]] + 1  # i=j'+1
                w[s[j]] = j  # 替换j'
                j += 1
        return ans

    # Q209 长度最小的子数组  滑动窗口O(n) d200227
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        ans = l + 1  # 如果不存在则最后为0
        sum = 0
        i = 0
        j = 0
        while j < l:
            sum += nums[j]
            while sum >= s:  # 以j为止的最短子数组
                ans = min(ans, j-i+1)
                sum -= nums[i]
                i += 1
            j += 1
        return ans if ans <= l else 0

    # Q209 长度最小的子数组 暴力O(n^3)  d200228  #######Points
    # 暴力优化 连续子数组和sum(from i to j) = sums[j]-sums[i] 遍历i O(n) 找j第一个使sum>=s O(n) O(n^2)
    # 二分查找 O(nlgn) 找j的过程可以优化为二分查找 sum(from i to j) 在i固定的随着j的递增而递增 有序查找第一个使sum>=s的j 可以用二分查找
    def minSubArrayLen_2(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        ans = l + 1
        sums = [0]  # sums[0] = 0, sums[1] = sums[0] + nums[0] sums[2] = sums[1] + nums[1]
        for i in range(0, l):
            sums.append(sums[i] + nums[i])  # sums[i+1]=sums[i]+sums[i]
        if sums[-1] < s:
            return 0
        for i in range(0, l):
            # sums[i] = nums[0] + nums[1] + ... + nums[i-1]
            # sums[j] = nums[0] + nums[1] + ... + nums[i-1] + nums[i] + ... + nums[j-1]
            # sum[ij) > s sums[j] - sums[i] > s 即找sums[j]> s + sums[i] 区间是itoj-1
            target = sums[i] + s
            low = i
            high = l - 1
            while low <= high:
                mid = low + (high - low) // 2
                if target >= sums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            j = high + 1
            ans = min(ans, j-i+1)
        return ans



if __name__ == "__main__":
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring_2("abcabcbb"))
    print(s.minSubArrayLen(7, [5, 1, 2, 4, 3]))
    print(s.minSubArrayLen_2(7, [5, 1, 2, 4, 3]))
