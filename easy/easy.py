# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : easy.py
# @Time     : 2020.01.08

from typing import List


class Solution:
    # Q1 两数之和 解法一 两层循环 7400 ms O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    return [i, i + j + 1]

    # Q1 两数之和 解法二 哈希(Python中即dict) 40 ms O(n)
    # 这道题本质是查找target-nums[i]在nums中的位置 查找->哈希
    # 边检查每个元素的target-nums[i]是否存在在之前建立的字典中
    # 边将nums数组中每个元素的值nums[i]与索引i添加进字典
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            else:
                dic[num] = i  # 因为只有一个答案，所以不可能存在[2,2,7] 9 第二个2代替第一个2的情况

    # Q167 两数之和II numbers是升序数组 双指针解法 O(n)
    # 两个指针low/high指向头尾 头尾元素加起来小于target则头指针后移，大于则尾指针前移
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            elif sum > target:
                high -= 1


    # Q7
    def reverse(self, x: int) -> int:
        if x < 0:
            is_negative = True
            x = -x
        str_x = str(x)
        result = int(str_x[::-1])  # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
        result = result if not is_negative else -result
        # result = result if -(1>>31) < x <

    # Q7 optimization for C
    def reverse_2(self, x: int) -> int:
        num = x if x > 0 else -x
        result = 0
        while num:
            result = result * 10 + (num % 10)
            num = num // 10
        if result > (1 << 31) - 1 or result < - (1 >> 31):
            return 0
        return result if x > 0 else -result

    # Q9
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ltr = x
        rtl = 0
        while x:
            rtl = rtl * 10 + x % 10
            x //= 10
        if ltr == rtl:
            return True
        else:
            return False

    # Q20 Stack
    def isValid(self, s: str) -> bool:
        s_list = []
        for i in s:
            if len(s_list) == 0:
                s_list.append(i)
            else:
                if i == ')' and s_list[-1] == '(' or i == ']' and s_list[-1] == '[' or i == '}' and s_list[-1] == '{':
                    s_list.pop()
                else:
                    s_list.append(i)
        if len(s_list) != 0:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    # print(s.twoSum([1, 2, 3, 4], 5))  # (0, 3)
    # print(s.twoSum([3, 3], 6))  # (0, 1)
    print(s.twoSum2([2, 7, 11, 15], 9))
    # print(s.reverse(123))
    # print(s.reverse(1534236469))
    # print(s.isPalindrome(20))
    # print(s.isValid("()[{]"))
