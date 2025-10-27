# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def length(self, head: Optional[ListNode]):
    #     ans = 0
    #     while head:
    #         ans += 1
    #         head = head.next
    #     return ans

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        for i in range(n):
            first = first.next
        if first is None:
            return head.next
        while first.next:
            second = second.next
            first = first.next
       
        second.next = second.next.next
        return head
        