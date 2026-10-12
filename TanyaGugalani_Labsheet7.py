#Ques1

'''import heapq

# ---------------- MIN HEAP / PRIORITY QUEUE ----------------

priority_queue = []

# Insert elements
heapq.heappush(priority_queue, 30)
heapq.heappush(priority_queue, 10)
heapq.heappush(priority_queue, 20)
heapq.heappush(priority_queue, 5)

print("Priority Queue (Min Heap):", priority_queue)

# Remove highest priority element (smallest)
print("Removed element:", heapq.heappop(priority_queue))

print("After removal:", priority_queue)


# ---------------- MAX HEAP ----------------

max_heap = []

numbers = [30, 10, 20, 5, 40]

for num in numbers:
    heapq.heappush(max_heap, -num)

print("\nMax Heap:")

while max_heap:
    print(-heapq.heappop(max_heap), end=" ")


# ---------------- HEAP SORT ----------------

def heap_sort(arr):
    heap = []

    # Insert all elements into heap
    for element in arr:
        heapq.heappush(heap, element)

    # Remove elements in sorted order
    sorted_array = []
    while heap:
        sorted_array.append(heapq.heappop(heap))

    return sorted_array


arr = [40, 10, 30, 50, 20, 5]

print("\n\nOriginal Array:", arr)
print("Sorted Array:", heap_sort(arr))'''


# Problem 2: Rearrange Array to Maximize Adjacent Sum Difference

'''def make_arrangement(arr, pattern):
    a = sorted(arr)
    n = len(a)

    result = [0] * n

    # Positions according to coefficient
    minus2 = [i for i in range(n) if pattern[i] == -2]
    minus1 = [i for i in range(n) if pattern[i] == -1]
    plus1 = [i for i in range(n) if pattern[i] == 1]
    plus2 = [i for i in range(n) if pattern[i] == 2]

    left = 0
    right = n - 1

    # Smallest values go to -2
    for i in minus2:
        result[i] = a[left]
        left += 1

    # Next smallest values go to -1
    for i in minus1:
        result[i] = a[left]
        left += 1

    # Largest values go to +2
    for i in reversed(plus2):
        result[i] = a[right]
        right -= 1

    # Remaining largest values go to +1
    for i in plus1:
        result[i] = a[right]
        right -= 1

    total = sum(abs(result[i] - result[i + 1]) for i in range(n - 1))

    return result, total


def maximize_difference(arr):
    n = len(arr)

    if n <= 1:
        return arr, 0

    if n == 2:
        return sorted(arr), abs(arr[0] - arr[1])

    # Pattern 1
    if n % 2 == 0:
        pattern1 = [1]
        for i in range(n - 2):
            pattern1.append(-2 if i % 2 == 0 else 2)
        pattern1.append(-1)

        pattern2 = [-1]
        for i in range(n - 2):
            pattern2.append(2 if i % 2 == 0 else -2)
        pattern2.append(1)

    else:
        pattern1 = [1]
        for i in range(n - 2):
            pattern1.append(-2 if i % 2 == 0 else 2)
        pattern1.append(1)

        pattern2 = [-1]
        for i in range(n - 2):
            pattern2.append(2 if i % 2 == 0 else -2)
        pattern2.append(-1)

    arr1, sum1 = make_arrangement(arr, pattern1)
    arr2, sum2 = make_arrangement(arr, pattern2)

    if sum1 >= sum2:
        return arr1, sum1
    else:
        return arr2, sum2

arr = list(map(int, input("Enter array elements: ").split()))

result, maximum_sum = maximize_difference(arr)

print("Rearranged Array:", result)
print("Maximum Sum:", maximum_sum)'''

#Ques3
# Problem 3: Smallest Subarray with Sum Greater Than Target

def smallest_subarray(arr, target):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        # Shrink the window while sum is greater than target
        while current_sum > target:
            min_length = min(min_length, right - left + 1)

            current_sum -= arr[left]
            left += 1

    if min_length == float('inf'):
        return -1

    return min_length


# Input
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

# Output
answer = smallest_subarray(arr, target)

print("Smallest Subarray Length:", answer)
