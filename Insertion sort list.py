# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        another_head = ListNode(0)
        another_head.next = None
        p = head
        while p != None:
            move_p = another_head
            while move_p.next != None and move_p.next.val < p.val:
                move_p = move_p.next
            temp_p = p
            p = p.next
            temp_p.next = move_p.next
            move_p.next = temp_p
        return another_head
        
