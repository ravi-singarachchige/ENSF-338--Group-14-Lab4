Question 1:

Arrays:

Advantages: 
Direct access to elements using indices, which makes access time O(1). 
Efficient when the size is known and constant.

Disadvantages: 
Insertion and deletion operations are costly, O(n), as the elements need to be shifted. 
Size needs to be known at the time of declaration, not dynamic.

Linked Lists:

Advantages: Dynamic size. Efficient insertion and deletion operations (O(1) if we have a pointer to the node).

Disadvantages: Access time is O(n) as elements are not stored contiguously and we need to traverse the list.

Question 2:

For arrays, a replace function can be implemented as a direct assignment operation at the given index, which is O(1). This avoids the need for deletion and insertion, which would be O(n) operations.

Question 3:

Insertion Sort: 
Feasible. We can traverse the list and insert elements at the correct position. Complexity is O(n^2).

Merge Sort: 
Not feasible directly as it requires random access, which linked lists do not support. However, it can be adapted for linked lists with a complexity of O(n log n).

Question 4:

Insertion Sort: 
For both arrays and linked lists, the complexity is O(n^2). However, linked lists require more space for pointers.

Merge Sort: 
For arrays, the complexity is O(n log n). For linked lists, merge sort is not directly applicable due to the lack of random access. However, an adapted version also has a complexity of O(n log n), but with additional space complexity due to the use of pointers.

