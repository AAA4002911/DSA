class Node {
    constructor(data) {
        this.val = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
        this.temp = null;
    }
    // Print Linked List
    print() {
        let temp = this.head;
        let result = "";
        while (temp !== null) {
            result += temp.val + " ";
            temp = temp.next;
        }
        console.log(result);
    }

    // Push Element to the end of Linked List
    push(val) {
        let node = new Node(val);
        if (this.head == null) {
            this.head = node;
            this.temp = node;
        }
        else {
            this.temp.next = node;
            this.temp = node;
        }
        this.size++;
    }
}

var deleteDuplicates = function(head) {
    let curr = head;
    let prev = null;
    while (curr != null) {
        if (prev != null && prev.val === curr.val) {
            prev.next = curr.next;
        } else {
            prev = curr;
        }
        curr = curr.next;
    }
    return head;
};
let arr = [1,1,2,2,2,3,3,3];
let ll = new LinkedList();
for (let i of arr) {
    ll.push(i);
}
deleteDuplicates(ll.head);
ll.print()