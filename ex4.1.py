#ex4.1

#Question 1

# Complexity Analysis of Provided Code:
#Best Case Complexity: The best case occurs when no elements in the list are greater than 5. In this case, the outer loop executes n times (where n is the size of the list), but the inner loop does not execute. Thus, the best case complexity is O(n).
#Worst Case Complexity: The worst case occurs when all elements in the list are greater than 5, causing the inner loop to execute for each element of the list. Since the inner loop also runs n times for each element, the worst case complexity is O(n^2).
#Average Case Complexity: The average case depends on the distribution of the elements in the list but will likely be closer to the worst case than the best case, especially as the size of the list grows, because the probability that at least some elements are greater than 5 increases. Thus, the average case complexity can also be considered as O(n^2) for large n, although it may vary based on the exact distribution of elements.
#This analysis is justified based on the number of operations performed by the loops in the code: the outer loop runs n times, and the inner loop's execution depends on the condition of elements being greater than 5, leading to a variable number of operations that can range from n (best case) to n^2 (worst case).

#Question 2
#No, they are not the same.
#MODIFIED CODE:
#def processdata(li):
    for i in range(len(li)):
        li[i] = li[i] * 2  # double the element
