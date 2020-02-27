# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : middle.py
# @Time     : 2020.02.25

from typing import List


class Solution:

    # Q15 三数之和 a+b+c=0 排序 固定a 双指针如Q167查找b+c O(n^2)+O(nlgn)=O(n^2)  d200225
    # 暴力求解O(n^3)  看作是a+b查找-a-b O(nlgn)  看作固定a双指针查找b+c O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()  # 排序
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

    # Q16 最接近的三数之和 排序+双指针 O(n^2)+O(nlgn)  d200226
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        ans = nums[0] + nums[1] + nums[-1] - target  # 不要自己设初值，而是从数组中抽取三个数假设最小
        for i, a in enumerate(nums):
            low = i + 1
            high = l - 1
            while low < high:
                new = a + nums[low] + nums[high] - target
                if abs(new) <= abs(ans):
                    ans = new
                if new > 0:
                    high -= 1
                elif new < 0:
                    low += 1
                else:
                    return target  # 差距为0
        return ans + target

    # Q18 四数之和 三数和基础上多加一层循环  d200226
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        if l < 4:
            return []
        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            for j, b in enumerate(nums[i+1:]):
                if j > 0 and b == nums[i+j]:
                    continue
                low = i + 1 + j + 1
                high = l - 1
                while low < high:
                    sum = a + b + nums[low] + nums[high]
                    if sum == target:
                        ans.append([a, b, nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif sum < target:
                        low += 1
                    else:
                        high -= 1
        return ans  # [0, 0, 0, 0]

    # Q454 四数之和II 暴力搜索TLE 拆分成二循环+hash可以过 O(n^2)  d200226
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        dic = {}  # 数：次数
        for a in A:
            for b in B:
                if a+b in dic:
                    dic[a+b] += 1
                else:
                    dic[a+b] = 1
        for c in C:
            for d in D:
                if 0-c-d in dic:
                    ans += dic[0-c-d]
        return ans


if __name__ == "__main__":
    s = Solution()
    # print(s.threeSum([0,0,0]))
    # print(s.threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0))
    # print(s.fourSum([1,0,-1,0,-2,2], 0))
    print(s.fourSumCount([0,1,-1], [-1,1,0], [0,0,1], [-1,1,1]))
