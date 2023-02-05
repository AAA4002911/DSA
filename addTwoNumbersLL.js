// TLE

var addTwoNumbers = function (l1, l2) {
    function reverseNum(num) {
        let x = num;
        let result = 0;
        while (x != 0) {
            let remainder = x % 10;
            result = 10 * result + remainder;
            x = parseInt(x / 10);
        }
        return result;
    }

    let temp = l1;
    let digit1 = 0;
    while (temp != null) {
        digit1 = 10 * digit1 + temp.val;
        temp = temp.next;
    }

    temp = l2;
    let digit2 = 0;
    while (temp != null) {
        digit2 = digit2 * 10 + temp.val;
        temp = temp.val;
    }
    digit1 = l1, digit2 = l2;
    digit1 = reverseNum(digit1);
    digit2 = reverseNum(digit2);
    let result = digit1 + digit2;
    result = reverseNum(result);
    console.log(result);


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

    let resultLL = new LinkedList();
    while (result != 0) {
        let remainder = result % 10;
        resultLL.push(remainder);
        result = parseInt(result / 10);
    }

    return resultLL.head;
};

addTwoNumbers(243, 564);

// Optimised Solution 

var addTwoNumbers = function(l1, l2) {
    let num = 0;
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

    let resultLL = new LinkedList();
    
    while (l1 != null || l2 != null || num != 0) {
        num += (l1 ? l1.val : 0) + (l2 ? l2.val : 0);
        resultLL.push(num % 10);
        num = parseInt(num / 10);
        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }
    
    return resultLL.head
};