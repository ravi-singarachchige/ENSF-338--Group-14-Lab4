Question 1:
Time complexity of reverse function is O(n^2). This is because 
the for loop runs n times, where n is the size of the linked list(self.get_size()).
Inside the for loop, we are calling get_element_at_pos function each time, which runs in O(n) time.
So, the time complexity of reverse function is O(n^2).

Question 2:
The unoptimised reverse function has a time complexity of O(n^2) because for each node in the list,
we are iterating through the list to find the node at the given position. But this method is not efficient
and we can do this without iterating through the list for each element by reversing the list in place. This can 
be done by iterating through the list once, keeping track of the previous node and the next node for each node, 
and reversing the link direction for each node. This will result in a time complexity of O(n) because we iterate 
through the list once and will be a more efficient way of reversing the list.

