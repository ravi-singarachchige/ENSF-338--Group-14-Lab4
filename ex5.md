Question 1

When timing a program, several types of noise can affect the measurement. 
These include system load, CPU scheduling, memory management, and hardware differences. 
Both timeit.timeit() and timeit.repeat() help mitigate these issues.
timeit.timeit() runs a code snippet a specified number of times and returns the total execution time. 
By running the code multiple times, it helps average out the noise and provides a more accurate estimate of the code's execution time. 
It's appropriate to use timeit.timeit() when you want a general estimate of how long a code snippet takes to run.
timeit.repeat() runs timeit.timeit() multiple times and returns a list of results. 
This helps identify the variability in execution times, which can be caused by the aforementioned noise. 
It's appropriate to use timeit.repeat() when you want to understand the distribution of execution times and identify outliers.

Question 2

timeit.timeit(): 
Since it returns the total time for a number of executions, the most appropriate statistic isaverage. 
This gives you the average time taken for a single execution of the code snippet.

timeit.repeat(): 
Since it returns a list of times, all three statistics (average, min, max) can be useful. 
The average gives you a general idea of the execution time, while the min and max can help identify the range of execution times and any outliers.



