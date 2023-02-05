var reverseList = function(head) {
    let prev = null;
    let curr = head;
    let future = head;
    while (future != null) {
        future = future.next;
        curr.next = prev;
        prev = curr;
        curr = future;
    }
    return prev;
};