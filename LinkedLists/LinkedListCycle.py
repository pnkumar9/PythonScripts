'''
141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

'''
Approach 2: Two Pointers
Intuition

Imagine two runners running on a track at different speed. What happens when the track is actually a circle?

Algorithm

The space complexity can be reduced to O(1)O(1) by considering two pointers at different speed - a slow pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.

Now consider a cyclic list and imagine the slow and fast pointers are two runners racing around a circle track. The fast runner will eventually meet the slow runner. Why? Consider this case (we name it case A) - The fast runner is just one step behind the slow runner. In the next iteration, they both increment one and two steps respectively and meet each other.

How about other cases? For example, we have not considered cases where the fast runner is two or three steps behind the slow runner yet. This is simple, because in the next or next's next iteration, this case will be reduced to case A mentioned above.
'''
def using_two_pointers(self, head):
        if not head: return False
        slow = head
        fast = head.next
        while slow and fast and fast != slow and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow == fast
    
 '''
 Approach 1: Hash Table
Intuition

To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.

Algorithm

We go through each node one by one and record each node's reference (or memory address) in a hash table. 
If the current node is null, we have reached the end of the list and it must not be cyclic. 
If current node’s reference is in the hash table, then return true.

Complexity analysis

Time complexity : O(n)O(n). We visit each of the nn elements in the list at most once. Adding a node to the hash table costs only O(1)O(1) time.

Space complexity: O(n)O(n). The space depends on the number of elements added to the hash table, which contains at most nn elements.

 '''   
def using_dict(self, head):
    mem = {}
    temp = head
    while temp:
        if temp in mem: return True
        else: mem[temp]= True
        temp = temp.next
    return False
