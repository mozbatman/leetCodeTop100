# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:23:06 2020

@author: -
"""

## ADD TWO NUMBER 


## You are given two non-empty linked lists representing two non-negative integers.
## The digits are stored in reverse order and each of their nodes contain a single digit. 
## Add the two numbers and return it as a linked list.

## Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
## Output: 7 -> 0 -> 8
## Explanation: 342 + 465 = 807.


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    
    def sonuc(self,l1: ListNode):
        val = l1
        i = 0
        sum = 0
        while val is not None:
            sum += val.val * pow(10,i)
            val = val.next
            i += 1
        sum = int(str(sum))
        return sum
          
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            a = self.sonuc(l1)
            b = self.sonuc(l2)
            ab = a + b
            print(ab)
            son = list(str(ab))
            lson = ListNode(son.pop(0))
            for i in son:
                gec = ListNode(int(i))
                gec.next = lson
                lson = gec
            return lson
        
        

        
        

if __name__ == "__main__":
    
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l2.next = l3
    l1.next = l2
    
    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l5.next = l6
    l4.next = l5
    
    s1 = Solution()
    s1.addTwoNumbers(l1,l4)
    