def delNode(head, k):
    # Code here
    if k==1:
        temp = head
        head = temp.next
    else:
        count = 0
        temp = head
        prev = None
        while temp.next != None:
            count+=1;
            if count==k:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
    return head