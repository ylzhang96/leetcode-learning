# -*- coding: utf-8 -*-
# @Author   : Yanli Zhang
# @Contact  : ylzhang96@163.com
# @Github   : https://github.com/ylzhang96
# @Project  : leetcode-learning
# @FileName : easy2.py.py
# @Time     : 2020.02.25

from typing import List


class Solution:
    # Q58 最后一个单词的长度 d200225
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1]) if len(s.strip()) > 0 else 0

    # Q929 独特的电子邮件地址 集合 d200225
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            two_part = email.split("@")
            local = two_part[0]
            if email.find("+") != -1:
                local = local[:email.find("+")]
            local = local.replace(".", "")
            new_email = local + "@" + two_part[1]
            s.add(new_email)
        return len(s)

if __name__ == "__main__":
    s = Solution()
    # print(s.lengthOfLastWord(" "))
    print(s.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]))