'''
206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

'''
A very nice explanation in this video
https://www.youtube.com/watch?v=XDO6I8jxHtA
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            
        return prev            
        