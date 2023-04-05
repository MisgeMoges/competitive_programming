/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
   public ListNode detectCycle(ListNode head) {
    ListNode tortoise = head;
    ListNode hare = head;
    
    // find meeting point
    while (hare != null && hare.next != null) {
        tortoise = tortoise.next;
        hare = hare.next.next;
        
        if (tortoise == hare) {
            // there is a cycle
            break;
        }
    }
    
    if (hare == null || hare.next == null) {
        // no cycle
        return null;
    }
    
    // find start of cycle
    tortoise = head;
    while (tortoise != hare) {
        tortoise = tortoise.next;
        hare = hare.next;
    }
    
    return tortoise;
}

}