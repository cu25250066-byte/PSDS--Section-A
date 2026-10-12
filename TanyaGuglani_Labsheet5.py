# Ques 1 
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, x):
#         self.stack.append(x)

#     def pop(self):
#         return self.stack.pop()

#     def peek(self):
#         return self.stack[-1] if self.stack else None

#     def empty(self):
#         return len(self.stack) == 0


# def priority(op):
#     if op == '+' or op == '-':
#         return 1
#     if op == '*' or op == '/':
#         return 2
#     if op == '^':
#         return 3
#     return 0


# def infix_to_postfix(exp):
#     s = Stack()
#     result = ""

#     for ch in exp:
#         if ch.isalnum():
#             result += ch

#         elif ch == '(':
#             s.push(ch)

#         elif ch == ')':
#             while not s.empty() and s.peek() != '(':
#                 result += s.pop()
#             if not s.empty():
#                 s.pop()

#         else:
#             while (not s.empty() and s.peek() != '('
#                    and priority(s.peek()) >= priority(ch)):
#                 result += s.pop()
#             s.push(ch)

#     while not s.empty():
#         result += s.pop()

#     return result


# exp = input("Enter infix expression: ")
# print("Postfix expression:", infix_to_postfix(exp))

# Ques 2
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, x):
#         self.stack.append(x)

#     def pop(self):
#         return self.stack.pop()


# def evaluate(exp):
#     s = Stack()

#     for ch in exp:
#         if ch.isdigit():
#             s.push(int(ch))

#         elif ch in "+-*/":
#             b = s.pop()
#             a = s.pop()

#             if ch == '+':
#                 s.push(a + b)
#             elif ch == '-':
#                 s.push(a - b)
#             elif ch == '*':
#                 s.push(a * b)
#             elif ch == '/':
#                 s.push(a / b)

#     return s.pop()


# exp = input("Enter postfix expression: ")
# print("Result:", evaluate(exp))

# Ques 3
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if data < root.data:
        return search(root.left, data)

    return search(root.right, data)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

n = int(input("Enter number of elements: "))

for i in range(n):
    data = int(input("Enter an element: "))
    root = insert(root, data)

print("Inorder traversal:", end=" ")
inorder(root)

print("\nPreorder traversal:", end=" ")
preorder(root)

print("\nPostorder traversal:", end=" ")
postorder(root)

data = int(input("\nEnter element to search: "))

if search(root, data):
    print("Element found")
else:
    print("Element not found")

data = int(input("Enter element to delete: "))
root = delete(root, data)

print("After deletion:")

print("Inorder traversal:", end=" ")
inorder(root)

print("\nPreorder traversal:", end=" ")
preorder(root)

print("\nPostorder traversal:", end=" ")
postorder(root)
