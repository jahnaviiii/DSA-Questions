# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]):
        ans = 0
        while head:
            ans += 1
            head = head.next
        return ans

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenn = self.length(head)
        pos = lenn - n

        if pos == 0:
            return head.next
        temp = head

        for i in range(pos - 1):
            temp = temp.next
        
        temp.next = temp.next.next
    
        return head