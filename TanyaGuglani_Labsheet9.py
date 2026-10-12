def solve(N, A):
    operations = 0

    for i in range(N):
        if A[i] > 0:
            return -1

        operations += abs(A[i])

    return operations


T = int(input("Enter number of test cases: "))

for t in range(T):
    N = int(input("Enter size of array: "))

    A = list(map(int, input("Enter array elements: ").split()))

    result = solve(N, A)

    print("Minimum operations:", result)
