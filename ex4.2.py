#ex.4.2


#Question3

#Inefficient Implementation(Linear Search):
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Target not found

#Efficient Implementation(Binart Search):
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

#Question 4
#The worst-case complexity for each provided code snippet is as follows:

#Linear Search
#The worst-case scenario occurs when the target element is not present in the array or is at the last position, requiring the algorithm to check each element exactly once. Thus, the worst-case complexity of linear search is O(n), where n is the number of elements in the array.

#Binary Search
#The worst-case scenario for binary search happens when the target element is not present in the array, or it is located at the beginning or end of the array, requiring the algorithm to halve the search space until it narrows down to a single element. The worst-case complexity of binary search is O(log n), where n is the number of elements in the array. This logarithmic complexity comes from the fact that with each comparison, binary search halves the number of elements to be searched, leading to a significantly faster search time compared to linear search for large datasets.

#Question 5
import timeit
import matplotlib.pyplot as plt


def measure_time(search_function, data, target):
    start_time = timeit.default_timer()
    search_function(data, target)
    end_time = timeit.default_timer()
    return end_time - start_time

# Generate data for the experiment
data_sizes = [1000, 2000, 4000, 8000]
linear_times = []
binary_times = []

for size in data_sizes:
    data = list(range(size))  # Sorted data
    target = -1  # Worst case scenario 
    
    # Measure time for linear search
    linear_time = measure_time(linear_search, data, target)
    linear_times.append(linear_time)
    
    # Measure time for binary search
    binary_time = measure_time(binary_search, data, target)
    binary_times.append(binary_time)

# Plotting the results
plt.plot(data_sizes, linear_times, label='Linear Search')
plt.plot(data_sizes, binary_times, label='Binary Search')
plt.xlabel('Data Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()






