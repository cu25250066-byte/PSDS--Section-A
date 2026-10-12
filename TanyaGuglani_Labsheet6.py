'''# Ques 1 
a = 1
b = 1
for i in range(5):
    print(a, end=" ")
    c = a + b
    a = b
    b = c'''
#Ques 2 
'''arr = [-3, 1, 2, 5, 6, -3, 8, 1, 9, 2]

result = set()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                result.add(tuple(sorted((arr[i], arr[j], arr[k]))))

print(result)'''
# Ques 3 
'''def tower(n, source, helper, destination):

    if n == 1:
        print(source, "->", destination)
        return

    tower(n - 1, source, destination, helper)

    print(source, "->", destination)

    tower(n - 1, helper, source, destination)


n = int(input("Enter number of disks: "))

tower(n, "A", "B", "C")
'''
