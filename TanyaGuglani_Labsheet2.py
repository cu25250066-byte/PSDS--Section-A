'''Ques 1 
# Linear Search
def linear_search(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


arr = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")'''
'''# Ques 2 
# Binary Search

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Take input from user
arr = list(map(int, input("Enter elements in sorted order: ").split()))
key = int(input("Enter the number to search: "))

result = binary_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")'''
