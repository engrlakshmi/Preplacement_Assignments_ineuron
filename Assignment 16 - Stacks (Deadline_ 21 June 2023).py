#!/usr/bin/env python
# coding: utf-8

# <aside>
# 💡 **Question 1**
# 
# Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.

# In[1]:


def findNearestGreaterFrequency(arr):
    stack = []
    frequency_map = {}
    n = len(arr)
    result = [-1] * n

    for i in range(n-1, -1, -1):
        frequency_map[arr[i]] = frequency_map.get(arr[i], 0) + 1
        while stack and frequency_map[arr[stack[-1]]] <= frequency_map[arr[i]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


# In[2]:


a= [1, 1, 2, 3, 4, 2, 1]
result=findNearestGreaterFrequency(a)
print(result)


# <aside>
# 💡 **Question 2**
# 
# Given a stack of integers, sort it in ascending order using another temporary stack.
# 
# </aside>
# 

# In[5]:


def sortStack(stack):
    temp_stack = []

    while stack:
        temp = stack.pop()

        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())

        temp_stack.append(temp)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack


# In[7]:


a=[34, 3, 31, 98, 92, 23]
result=sortStack(a)
print(result)


# <aside>
# 💡 **Question 3**
# 
# Given a stack with **push()**, **pop()**, and **empty()** operations, The task is to delete the **middle** element ****of it without using any additional data structure.
# 
# </aside>

# In[ ]:


def deleteMiddle(stack):
    stack_size = len(stack)
    count = 0
    mid = stack_size // 2

    new_stack = []
    while stack:
        temp = stack.pop()
        count += 1
        if count != mid:
            new_stack.append(temp)

    while new_stack:
        stack.append(new_stack.pop())

    return stack


# In[ ]:





# <aside>
# 💡 **Question 4**
# 
# Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:
# 
# 1. Push and pop elements from the stack
# 2. Pop (Or Dequeue) from the given Queue.
# 3. Push (Or Enqueue) in the another Queue.
# </aside>

# In[8]:


from queue import Queue

def checkIncreasingOrder(queue):
    stack = []
    otherQueue = Queue()
    expected = 1

    while not queue.empty():
        if queue.queue[0] == expected:
            queue.get()
            expected += 1
        elif stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            otherQueue.put(queue.get())

    while stack:
        if stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            return False

    return otherQueue.empty()

# Example usage
queue = Queue()
queue.put(2)
queue.put(3)
queue.put(1)
queue.put(4)

print(checkIncreasingOrder(queue))  # Output: True


# <aside>
# 💡 **Question 5**
# 
# Given a number , write a program to reverse this number using stack.
# 
# </aside>

# In[9]:


def reverseNumber(num):
    num_str = str(num)
    stack = []

    # Push each character onto the stack
    for char in num_str:
        stack.append(char)

    reversed_str = ""

    # Pop each character from the stack
    while stack:
        reversed_str += stack.pop()

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    return reversed_num


# <aside>
# 💡 **Question 6**
# 
# Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.
# 
# Only following standard operations are allowed on queue.
# 
# - **enqueue(x) :** Add an item x to rear of queue
# - **dequeue() :** Remove an item from front of queue
# - **size() :** Returns number of elements in queue.
# - **front() :** Finds front item.
# </aside>

# In[ ]:


from queue import Queue


def reverse_first_k(queue, k):
    if k <= 0 or k > queue.qsize():
        return

    stack = []
    for _ in range(k):
        stack.append(queue.get())

    while not queue.empty():
        queue.put(queue.get())

    while len(stack) > 0:
        queue.put(stack.pop())

    for _ in range(queue.qsize() - k):
        queue.put(queue.get())


# Example usage:
queue = Queue()
elements = [1, 2, 3, 4, 5, 6, 7]
for element in elements:
    queue.put(element)

k = 4
reverse_first_k(queue, k)

# Print the queue
while not queue.empty():
    print(queue.get(), end=" ")


# <aside>
# 💡 **Question 7**
# 
# Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.
# 
# </aside>

# In[ ]:


def count_remaining_words(sequence):
    stack = []
    for word in sequence:
        if not stack or word != stack[-1]:
            stack.append(word)
        else:
            stack.pop()

    return len(stack)


# Example usage:
sequence = ["apple", "banana", "banana", "kiwi", "orange", "kiwi", "apple"]
remaining_words = count_remaining_words(sequence)
print("Number of words left:", remaining_words)


# <aside>
# 💡 **Question 8**
# 
# Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.
# 
# **Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.
# 
# </aside>

# In[ ]:


def max_absolute_difference(arr):
    n = len(arr)
    left_smaller = [0] * n
    right_smaller = [0] * n
    stack = []

    # Find nearest smaller element on the left side
    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            left_smaller[i] = stack[-1]
        stack.append(arr[i])

    stack = []

    # Find nearest smaller element on the right side
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            right_smaller[i] = stack[-1]
        stack.append(arr[i])

    max_diff = 0

    # Calculate maximum absolute difference
    for i in range(n):
        diff = abs(left_smaller[i] - right_smaller[i])
        max_diff = max(max_diff, diff)

    return max_diff


# Example usage:
arr = [2, 4, 1, 9, 7, 5, 8]
result =max_absolute_difference(arr)
result


# In[ ]:




