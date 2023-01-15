def has_cycle(head):
    
    seen = set()
    while head:
        if head in seen:
            return 1
        else:
            seen.add(head)
        
        head = head.next
    return 0
