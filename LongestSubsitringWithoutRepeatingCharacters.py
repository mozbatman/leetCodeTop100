# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:34:18 2020

@author: -
"""

#  3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter, longest, hs = 0, 0, []
        for i in s:
            hs.append(i)
            counter = counter + 1
            if hs.count(i) > 1:
                start = hs.index(i) + 1
                counter = counter - start
                s = s[start:len(s)]
                hs.clear()
                # hs.append(s[0:counter-1])
                hs = hs + list(s[0:counter-1])

                hs.append(i)

            if len(hs) > longest:
                longest = len(hs)

        return longest
        
        
if __name__ == "__main__":
    s = "pwwkew"
    a = []
    a = Solution().lengthOfLongestSubstring(s)
    print(a)