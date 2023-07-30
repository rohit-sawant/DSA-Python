
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def array_to_linked_list(self,arr):
        if not arr:
            return None

        # Create the head node of the linked list
        head = ListNode(arr[0])
        current_node = head

        # Iterate through the array starting from index 1
        for i in range(1, len(arr)):
            new_node = ListNode(arr[i])
            current_node.next = new_node
            current_node = new_node

        return head
    def linked_list_to_array(self,head):
        arr = []
        current_node = head
        while current_node:
            arr.append(current_node.val)
            current_node = current_node.next
        return arr
    
        return arr
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = head
        while curr:
            prev =  dummy_head
            next = dummy_head.next
            while next:
                if curr.val < next.val:
                    break
                prev = prev.next
                next= next.next
            temp = curr.next
            curr.next = next
            prev.next = curr
            curr = temp

        return dummy_head.next
            


sol = Solution()
print(sol.linked_list_to_array (sol.insertionSortList(sol.array_to_linked_list([4,3,2,1]))))
