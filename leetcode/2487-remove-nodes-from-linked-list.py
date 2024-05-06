class Solution:
    def removeNodes(head):
        def reverse(head):
            prev, cur = None, head
            while cur:
                temp = cur.next #store the next node in the temp
                cur.next = prev #change the pointer to the previous node that i.e none
                prev, cur = cur, temp   #update the values prev to cur and cur to temp i.e cur.next
            return prev
            
        head = reverse(head)
        cur = head
        cur_max = cur.val
        while cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur_max = cur.next.val
                cur = cur.next
        return reverse(head)