arr = []

def push(value):
    arr.append(value)
    return arr

#print(push(4))

def pop():
    if len(arr) == 0:
        print('Stack is Empty')
        return None
    else:
        last_index = len(arr) - 1
        last_element = arr[last_index]
        # TODO :
        del arr[last_index]
        return last_element
print(pop())
print(push(1))
print(push(3))
print(pop())
print(push(5))
print(push(6))
print(pop())
print(pop())
print(pop())
print(pop())

