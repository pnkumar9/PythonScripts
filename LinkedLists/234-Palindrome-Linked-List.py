'''
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

'''
https://www.youtube.com/watch?v=oZuR2-AKkXE
idea:

1. split the LL in the middle
2. Prepare two LL.
3. If odd, ignore the middle node
4. reverse the second LL
5. Compare the two linked lists
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            
        return prev    

    def isPalindrome(self, head: ListNode) -> bool:
        
        #edge cases
        
        # if no node or single node return True
        if not head or not head.next: return True
        
        #if two nodes, compare two vales
        if not head.next.next: return head.next.val == head.val
        
        #split the LL in the middle
        
        fast = mid = head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        
        #now mid points to second half of the LL
        #now reverse second LL
        second = self.reverseLL(mid )
        
        #now compare
        
        first= head
        
        while first and second:
            
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
            
        return True
        
        
        
            
        # prepare two LL
        #if odd ignore the middle node
        # reverse second LL
        #compare both LLs
        
        