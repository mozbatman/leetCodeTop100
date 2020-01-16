# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:31:35 2020

@author: -
"""

# 1. Two Sum

#Given an array of integers, 
#return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        sozluk = {}
        
        for i, num in enumerate(nums):
            if num in sozluk:
                return [sozluk[num], i]
            else :
                a = target - num 
                sozluk[a] = i