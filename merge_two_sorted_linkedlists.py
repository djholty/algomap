# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        #create pointers to beginning of both lists and create new list
        plist1 = list1 #pointer to head of list one
        plist2 = list2 #pointer to head of list two
        #point new list to lowest valued pointer to create start of new list
        if plist1.val <= plist2.val:
            newlist = plist1
            plist1 = plist1.next
        else:
            newlist = plist2
            plist2 = plist2.next
        headnewlist = newlist
        #start looping through the lists taking the lowest node and linking it
        while plist1 != None and plist2 != None:
            if plist1.val <= plist2.val:
                newlist.next = plist1
                newlist = newlist.next
                plist1 = plist1.next
            else:
                newlist.next = plist2
                newlist = newlist.next
                plist2 = plist2.next

        #if one of the lists is still 
        if plist1 != None and plist2 == None:
            while plist1:
                newlist.next = plist1
                newlist = newlist.next
                plist1 = plist1.next
        elif plist2 != None and plist1 == None:
            while plist2:
                newlist.next = plist2
                newlist = newlist.next
                plist2 = plist2.next
        else:
            print('list both empty')
            
        return headnewlist

"""
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""


