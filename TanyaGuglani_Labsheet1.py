'''
Ques 1
import numpy as np

arr = np.array([1, 2, 3])

# Push
arr = np.append(arr, 4)
print("After push:", arr)

# Pop
arr = np.delete(arr, -1)
print("After pop:", arr)

arr = np.array([10, 20, 30, 40, 50])

while len(arr) > 0:
    popelement = arr[-1]
    print("Popping this item:", popelement)
    arr = np.delete(arr, -1)
    print("Array after pop:", arr)'''

'''
Ques 2
# Enqueue and Dequeue Operation

import numpy as np

# Create a queue
queue = np.array([10, 20, 30])

print("Original Queue:", queue)

# Enqueue operation
queue = np.append(queue, 40)

print("After Enqueue:", queue)

# Dequeue operation
dequeued_item = queue[0]

print("Dequeued Item:", dequeued_item)

queue = np.delete(queue, 0)

print("After Dequeue:", queue)'''
