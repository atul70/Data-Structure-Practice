import numpy as np
arr = []#np.array([])

rear_index = -1
front_index = 0

def enque(value):
    global rear_index
    arr.append(value)
    rear_index += 1
    return arr

def deque():
    global rear_index
    global front_index

    if front_index > rear_index or rear_index == -1:
        print('Queue Is Emtpy')
        return None
    else:
        deleted_value = arr[front_index]

        del arr[front_index]
        #front_index += 1
        return deleted_value

print(deque())
print(enque(1))
print(enque(3))
print(deque())
print(enque(5))
print(enque(6))
print(deque())
print(deque())
print(deque())
print(deque())

