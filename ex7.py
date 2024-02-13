class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def get_element_at_position(self, pos):
        curr = self.head
        for _ in range(pos):
            if not curr:
                return None
            curr = curr.next
        return curr

    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_position(i)
            if newhead is None:
                newhead = currNode
            else:
                prevNode.next = currNode
            prevNode = currNode
        self.head = newhead

#Question 2:

    def reverse_optimized(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


#Question 3:
    
import time
import matplotlib.pyplot as plt

sizes = [1000, 2000, 4000, 8000]
original_times = []
optimized_times = []

for size in sizes:
    # Create a list with 'size' elements
    list = LinkedList()
    for i in range(size):
        list.insert_head(Node(i))

    # Time the original reverse method
    start = time.time()
    for _ in range(10):
        list.reverse()  
    original_times.append(end - start)

    # Time the optimized reverse method
    start = time.time()
    for _ in range(10):
        list.reverse_optimized()
    end = time.time()
    optimized_times.append(end - start)

# Plot the results
plt.plot(sizes, original_times, label='Original')
plt.plot(sizes, optimized_times, label='Optimized')
plt.xlabel('List Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()