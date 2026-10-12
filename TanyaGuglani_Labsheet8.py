'''N, K = map(int, input("Enter N and K: ").split())

arr = list(map(int, input("Enter array elements: ").split()))

# Sum of first K elements
window_sum = sum(arr[:K])

max_sum = window_sum

# Slide the window
for i in range(K, N):
    window_sum = window_sum + arr[i] - arr[i - K]

    max_sum = max(max_sum, window_sum)

print("Maximum Sum:", max_sum)'''

#Ques 2
# Longest Substring Without Repeating Characters

'''s = input("Enter string: ")

left = 0
max_length = 0
characters = set()

for right in range(len(s)):

    # If character is already present,
    # remove characters from the left
    while s[right] in characters:
        characters.remove(s[left])
        left += 1

    # Add current character
    characters.add(s[right])

    # Calculate current window length
    current_length = right - left + 1

    # Update maximum length
    max_length = max(max_length, current_length)

print("Longest Substring Length:", max_length)'''

#Ques 3
import heapq

def shortest_path(n, edges, k):
    graph = [[] for _ in range(n + 1)]

    # Build undirected graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # (cost, node, edges_used)
    pq = [(0, 1, 0)]

    # Distance[node][edges]
    dist = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    dist[1][0] = 0

    while pq:
        cost, node, used = heapq.heappop(pq)

        if cost > dist[node][used]:
            continue

        if node == n:
            return cost

        if used == k:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            new_used = used + 1

            if new_cost < dist[neighbor][new_used]:
                dist[neighbor][new_used] = new_cost

                heapq.heappush(
                    pq,
                    (new_cost, neighbor, new_used)
                )

    return -1


# Input from user
n, m, k = map(int, input("Enter N, M, K: ").split())

edges = []

for _ in range(m):
    u, v, w = map(int, input("Enter u, v, weight: ").split())
    edges.append((u, v, w))

result = shortest_path(n, edges, k)

print("Minimum Path Weight:", result)
