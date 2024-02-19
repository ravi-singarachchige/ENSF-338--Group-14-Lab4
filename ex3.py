# Q1
# In the file called lists.c, the arrays are dynamically resized using a strategy known as geometric expansion. 
# This strategy involves doubling the size of the array each time it becomes full.
# The specific line of code where this strategy is implemented can be found in the list_resize function in the lists.c file. 
# In particular, the line "new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6);" calculates the new size for the array, effectively doubling it when it becomes full. 
# The growth factor in this case is 2, as the array size is doubled with each resize.


# Q2
def test_list_growth():
    lst = []
    prev_length = len(lst)

    for i in range(64):
        lst.append(i)
        new_length = len(lst)
        if new_length != prev_length:
            print(f"Capacity changed from {prev_length} elements to {new_length} elements at size {i}")
            prev_length = new_length

test_list_growth()



# Q3
import timeit

# Define a function to measure the time to grow the array from size S to S+1
def measure_growth_time(S):
    setup_code = f"""
lst = list(range({S}))
"""
    stmt = "lst.append(0)"
    return timeit.timeit(stmt, setup=setup_code, number=1000)

# Set the initial size S
S = 100

# Measure the time to grow the array from size S to S+1
time_taken = measure_growth_time(S)
print(f"Time taken to grow the array from size {S} to size {S+1}: {time_taken} seconds")



# Q4
import timeit

# Define a function to measure the time to grow the array from size S-1 to S
def measure_growth_time(S):
    setup_code = f"""
lst = list(range({S-1}))
"""
    stmt = "lst.append(0)"
    return timeit.timeit(stmt, setup=setup_code, number=1000)

# Set the initial size S
S = 100

# Measure the time to grow the array from size S-1 to S
time_taken = measure_growth_time(S)
print(f"Time taken to grow the array from size {S-1} to size {S}: {time_taken} seconds")



# Q5
import matplotlib.pyplot as plt

# Collect timing data for growing array from size S to S+1
growth_time_S_to_Splus1 = [measure_growth_time(S) for _ in range(1000)]

# Collect timing data for growing array from size S-1 to S
growth_time_Sminus1_to_S = [measure_growth_time(S - 1) for _ in range(1000)]

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.hist(growth_time_S_to_Splus1, bins=30, color='blue', alpha=0.7)
plt.title('Distribution of time to grow array from size S to S+1')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(2, 1, 2)
plt.hist(growth_time_Sminus1_to_S, bins=30, color='red', alpha=0.7)
plt.title('Distribution of time to grow array from size S-1 to S')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
# The plots are mostly similar as it takes more time for both implementations when the frequency is less. 
