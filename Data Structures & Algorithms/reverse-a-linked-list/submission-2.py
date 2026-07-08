# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursively
        # time O(n), space O(n)
        if not head:
            return None

        new_head = head # new_head keeps track of end of list; start of reversed ist
        if head.next:
            new_head = self.reverseList(head.next)
            (head.next).next = head # actually reverse pointer
        head.next = None

        return new_head