def create_stack():
    stack = list()  # declaring an empty list
    return stack


# Checking for empty stack
def Isempty(stack):
    return len(stack) == 0


# Inserting items into the stack
def push(stack, n):
    stack.append(n)


# Removal of an element from the stack
def pop(stack):
    if (Isempty(stack)):
        return "stack is empty"
    else:
        return stack.pop()

def show(stack):
    for i in stack:
        print(i)
