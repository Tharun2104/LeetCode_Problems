## Q1 - Explain in your own words what a linked list is?<br>
Linked lists are node-based data structures in which data is organized using nodes. Each node in a linked list contains two main parts the data and a reference (or link) to the next node in the sequence.<br>

**LinkedNode Class:** : This class represents a single node in the linked list. Each node has two parts:<br>
 - value: This is the actual data stored in the node.<br>
 - next: This is a reference to the next node in the linked list. If there's no next node, it is set to None.<br>
 - __repr__ : Returns the string representation of the node's value.<br>

**LinkedList Class** : It primarily keeps track of the first node in the list, known as the head.<br>
The LinkedList class includes various methods to manage the nodes, such as inserting, deleting and searching the node.

When you create a linked list using the LinkedList and LinkedNode classes, the list starts with the head set to None, indicating that it is empty. When you insert a node into this empty linked list, a new LinkedNode is created with the specified value, and the head is updated to this new node.

For example, when inserting a node at a specific index, you need to traverse the linked list to find the position just before the desired index. Once there, you save the reference to the next node. Then, you create a new LinkedNode and adjust the references set the current node's next to point to this new node, and set the new node's next to point to the node that was originally after the current node. This process effectively inserts the new node at the specified index in the linked list. This process demonstrates how the LinkedList and LinkedNode classes work together to insert a new node into the linked list.

The LinkedNode class defines each individual node, and the LinkedList class manages the collection of nodes, providing functionality to insert/delete and traverse the list.

## Q2 - Give the time complexity of the following operations and explain briefly why that is the case. 
    Insert at beginning
    Insert at end
    Delete from beginning
    Delete from end
    Search a value
    Find the index of a value

**Insert at beginning** : Time Complexity - O(1)
Inserting a new node at the beginning of a linkedlist doesnot depend on the size of the list. When you insert a new node at the beginning it will create a new node and updates its next to the current head. Then the head is updated to the new node. As all these operations are constant time - O(1).<br>

**Insert at end** : Time Complexity - O(N)
Insert a node at the end, you must traverse the entire list from the head to the last node which takes O(n){n is the number of nodes}. Once you reach last node you have to update the last node next to the new node and new node next to none. Thus, this operation has a time complexity is equal to the length of the linkedlist.<br>

**Delete from beginning** : Time Complexity - O(1)
Delete a node from the beginning means updating the head to the next node. This operation does not depend on the length of the list. Hence constant time the TC is O(1).<br>

**Delete from end** : Time Complexity - O(N)
Deleting a node from the end of the list, you need to traverse the entire list from the head to the last but one element. After reaching this node, you update its next reference to None to remove the last node. The traversal to find the last but one node takes linear time n(length of the list), so the operation's time complexity is O(n).<br>

**Search a value** : Time Complexity - O(N)
Searching for a value means going through the list from the head and checking each node's value until you find the target value or reach the end of the list. Since the time needed depends on the length of the list, this operation has linear time complexity.<br>

**Find the index of a value** : Time Complexity - O(N)
Finding the index of a value requires traversing the list from the head while keeping track of the index and checking each node’s value. Since the time needed depends on the length of the list, this operation has linear time complexity.

