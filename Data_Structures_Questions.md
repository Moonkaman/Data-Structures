Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1)
2. What is the runtime complexity of `dequeue`?
   O(1)
3. What is the runtime complexity of `len`?
   O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   O(log(n))
2. What is the runtime complexity of `contains`?
   O(log(n))
3. What is the runtime complexity of `get_max`?
   O(n/2)

## Heap

1. What is the runtime complexity of `_bubble_up`?
   O(log(n))
2. What is the runtime complexity of `_sift_down`?
   O(log(n))
3. What is the runtime complexity of `insert`?
   O(log(n))
4. What is the runtime complexity of `delete`?
   O(log(n))
5. What is the runtime complexity of `get_max`?
   O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
   O(1)
3. What is the runtime complexity of `ListNode.delete`?
   O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    I would think they would be about the same. I don't know exactly how array.splice works under the hood but based on this https://medium.freecodecamp.org/lets-clear-up-the-confusion-around-the-slice-splice-split-methods-in-javascript-8ba3266c29ae

    it looks like it just removes the element at the index you give it n amount of times. The delete method on the doubly linked list doesn't have a way to delete things multiple times in one call but it does the same thing essentially, take the node you give it and remove it. I suppose in worst case scenario for array.splice you could keep getting rid of things until that index wasn't there anymore in which case that would be O(n).
