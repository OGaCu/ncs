# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # O(n), O(1)
        # iteratve, keep a node before reverse 
        
        dummy = ListNode(0, head)
        # get leftPrev to node before reversing
        leftPrev = dummy
        for _ in range(left - 1):
            leftPrev = leftPrev.next
        curr = leftPrev.next

        # reverse right - left + 1 in place
        prev = None
        for _ in range(right - left + 1): # 3
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # stitch left to the next node of right
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
