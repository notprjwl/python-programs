# question is straight forward

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def deleteNode(self, node):
        while node.next.next != None:
            node.val = node.next.val
            cur = node
            node = cur.next
        cur.next = None
            
                
                    
    

        