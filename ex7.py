# Question 2 (coding part)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def get_element_at_pos(self, pos):
        count = 0
        current = self.head
        while current:
            if count == pos:
                return current
            count += 1
            current = current.next
        return None

    # unoptimised reverse function
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # optimised reverse function
    def reverse_optimised(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
        
# Question 3
import timeit

elapsedTimeReverse = 0
elapsedTimeReverseOptimised = 0
elapsedTimeReverseAvg = []
elapsedTimeReverseOptimisedAvg = []

for x in [1000, 2000, 3000, 4000]:
    for y in range(100):
        
        linked_list = LinkedList()
        for i in range(x):
            linked_list.insert_head(i)

        elapsedTimeReverse += timeit.timeit(lambda: linked_list.reverse(), number = 1)
        elapsedTimeReverseOptimised += timeit.timeit(lambda: linked_list.reverse_optimised(), number = 1)
	
    elapsedTimeReverseAvg.append(elapsedTimeReverse/100)
    elapsedTimeReverseOptimisedAvg.append(elapsedTimeReverseOptimised/100)


# Question 4
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1000, 2000, 3000, 4000])
y = np.array(elapsedTimeReverseAvg)
z = np.array(elapsedTimeReverseOptimisedAvg)

plt.plot(x, y, label = "Reverse")
plt.plot(x, z, label = "Reverse Optimised")
plt.xlabel('Size of the array')
plt.ylabel('Time taken to execute the function')
plt.title('Performance of reverse and reverse_optimised functions')
plt.legend()
plt.show()