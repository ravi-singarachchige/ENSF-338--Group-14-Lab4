import time
import array
import random
import numpy as np
import matplotlib.pyplot as plt

# Linked list class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def binary_search(self, num):
        start_time = time.time()
        current = self.head
        while current:
            if current.data == num:
                return time.time() - start_time
            current = current.next
        return -1

# Array class
class Array:
    def __init__(self, size):
        self.size = size
        self.arr = array.array('i', [0] * size)

    def binary_search(self, num):
        start_time = time.time()
        left = 0
        right = len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == num:
                return time.time() - start_time
            elif self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
#4. 
#Time Complexity of a linked list:
#In a linked list, we find the midpoint by traversing the list from the start. This, on average, takes O(n/2) time.
#In linked lists, we can't divide the data using the indices. We traverse through the data linearly. Thus, the time complexity is O(n). 

#5. 
# Generate sorted lists of integers for both linked list and array
linked_list = LinkedList()
array_list = Array(8000)

for size in [1000, 2000, 4000, 8000]:
    sorted_data = list(range(size))
    random.shuffle(sorted_data)  
    sorted_data.sort()  
    for num in sorted_data:
        linked_list.append(num)
        array_list.arr[size - 1] = num  

# Measure average time for binary search in linked list
linked_list_search_times = []
for size in [1000, 2000, 4000, 8000]:
    total_time = 0
    for _ in range(100):  # Perform 100 searches for each input size
        random_num = random.randint(0, size - 1)
        total_time += linked_list.binary_search(random_num)
    average_time = total_time / 100
    linked_list_search_times.append(average_time)

# Measure average time for binary search in array
array_search_times = []
for size in [1000, 2000, 4000, 8000]:
    total_time = 0
    for _ in range(100):  # Perform 100 searches for each input size
        random_num = random.randint(0, size - 1)
        total_time += array_list.binary_search(random_num)
    average_time = total_time / 100
    array_search_times.append(average_time)

#6. 
# Plot results
input_sizes = [1000, 2000, 4000, 8000]
plt.plot(input_sizes, linked_list_search_times, label='Linked List', marker='o')
plt.plot(input_sizes, array_search_times, label='Array', marker='x')

# Interpolate with appropriate functions
linked_list_interp = np.poly1d(np.polyfit(input_sizes, linked_list_search_times, 2))
array_interp = np.poly1d(np.polyfit(input_sizes, array_search_times, 2))
x_values = np.linspace(min(input_sizes), max(input_sizes), 100)
plt.plot(x_values, linked_list_interp(x_values), linestyle='--', color='blue', label='Linked List (Interpolated)')
plt.plot(x_values, array_interp(x_values), linestyle='--', color='orange', label='Array (Interpolated)')

plt.xlabel('Input Size')
plt.ylabel('Average Search Time (seconds)')
plt.title('Binary Search Performance')
plt.legend()
plt.grid(True)
plt.show()



