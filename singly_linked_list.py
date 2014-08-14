# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head != None and head.next != None:
            cur_p = head
            next_p = cur_p.next
            while next_p != None:
                if cur_p.val == next_p.val:
                    cur_p.next = next_p.next
                else:
                    cur_p = next_p
                next_p = next_p.next
        return head
