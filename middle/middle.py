# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : middle.py
# @Time     : 2020.02.25

from typing import List


class Solution:

    # Q15 三数之和 a+b+c=0 排序 固定a 双指针如Q167查找b+c O(n^2)+O(nlgn)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if a > 0:
                return ans
            if i > 0 and a == nums[i-1]:  # 去掉重复a元素 [-1 -1 0 1]
                continue
            low = i + 1
            high = l - 1
            while low < high:
                if a + nums[low] + nums[high] == 0:  # 去掉第三个-1 与第二个-1重复 [-1 -1 -1 0 1 2]
                    # print(a, nums[low], nums[high])
                    ans.append([a, nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif a + nums[low] + nums[high] < 0:
                    low += 1
                else:
                    high -= 1
        return ans  # [0,0,0]



if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([0,0,0]))