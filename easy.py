# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : easy.py
# @Time     : 2020.01.08

from typing import List   # https://www.jb51.net/article/166907.htm


class Solution:

    # Q1 O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    return [i, i+j+1]

    # Q2 O(n)
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], i]
            else:
                dic[num] = i

    # Q7
    def reverse(self, x: int) -> int:
        if x < 0:
            is_negative = True
            x = -x
        str_x = str(x)
        result = int(str_x[::-1])  # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
        return result if not is_negative else -result


    # Q7 optimization for C
    def reverse_2(self, x: int) -> int:
        num = x if x > 0 else -x
        result = 0
        while num:
            result = result * 10 + (num % 10)
            num = num // 10
        if result > (1<<31)-1 or result < - (1>>31):
            return 0
        return result if x > 0 else -result



if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1, 2, 3, 4], 5))  # (0, 3)
    print(s.twoSum([3, 3], 6))  # (0, 1)
    print(s.reverse(123))
    print(s.reverse(1534236469))