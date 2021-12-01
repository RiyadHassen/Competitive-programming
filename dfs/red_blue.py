# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:33:58 2021

@author: riyad
"""


def red_blue(l, s):
    count = 0
    prev = s[0]
    result = []
    if s[0] == "?":
        for i in range(len(s)):
            if s[i] == "?":
                count += 1
            elif s[i] == "B":
                prev = "B" if count % 2 == 0 else "R"
                break
            else:
                prev = "R" if count % 2 == 0 else "B"
                break
    if prev == '?':
        prev = 'B'
    result.append(prev)
    for i in range(1, len(s)):
        if s[i] == "?":
            if prev == "B":
                result.append("R")

            else:
                result.append("B")
        else:
            result.append(s[i])
        prev = result[-1]

    return "".join(result)


if __name__ == '__main__':
    t = eval(input())
    for i in range(t):
        l = eval(input())
        s = input()
        print(red_blue(l, s))
