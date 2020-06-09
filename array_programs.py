# Program 1 - Program for array rotation
"""
array = [12,3,10,9,8,33,7,87,54]
#print(len(array)//2)
swap_index = -1
for i in range(0,len(array)//2):
    #print(array[i])
    a = array[i]
    #print(a)
    array[i] = array[-1-i]
    array[-1-i] = a
    swap_index = -i

print(array)

"""
# Program 2 -  Reversal algorithm for array rotation
"""
#Time Complexity : O(n)
#Space Complexity : O(n)
#---------------------------------

arr = [12,3,10,9,8,33,7,87,54]
req_rotation = 2
length = len(arr)
rem_elems = length-req_rotation

new_arr = []

for i in range(req_rotation, length):
    new_arr.append(arr[i])
for i in range(0, req_rotation):
    new_arr.append(arr[i])

print(new_arr)
"""

"""

arr = [12,3,10,9,8,33,7,87,54]
req_rotation = 2
length = len(arr)


for i in range(0, req_rotation):
    val = arr[0]
    for j in range(1, length):
        arr[j-1] = arr[j]
    arr[length-1] = val
print(arr)

"""


# Program to cyclically rotate an array by one
"""
a = [21,11,54,2,31,98,90]
length = len(a)
for i in range(0, length,-1):

    first = a[i]
    #if i < length-1:
       # a[i] = a[i+1]
    #for j in range(i+1, len(a)):
        #a[j-1] = a[j]
a[length-1] = first
print(a)
"""

# Split the array and add the first part to the end\
"""
arr = [12,2,11,91,32,8,43,35]
split = 3
n= len(arr)
new_arr = []
for j in range(split, n):
     new_arr.append(arr[j])
for i in range(0, split):
     new_arr.append(arr[i])
print(new_arr)

"""

#Find element at given index after a number of rotations

"""

arr = [32,65,12,90,88,71,43,4,20]
ranges = 2
index = 3
n = len(arr)

for i in range(0,ranges):
    val = arr[0]
    for j in range(1,n):
        arr[j-1] = arr[j]
    arr[n-1] = val
print(arr)
print(arr[index])

"""

#Reversal algorithm for right rotation of an array
"""
arr = [21,3,2,11,54,32,98,10]
right_rot = 2

for j in range(0, right_rot):
    n = len(arr)
    last_ele = arr[n-1]
    counter = n-1
    for i in range(0, n-1):
        arr[counter] = arr[counter-1]
        counter = counter - 1

    arr[0] = last_ele

print(arr)

"""



#print(arr)


"""
right_rot = 3
n = len(arr)
remain = n - right_rot

for i in range(0, right_rot):
    val = arr[-i-1]
    print(val)
    for j in range(0, remain):

        #arr[n] = arr[n-1]
        temp = arr[j]
        arr[j] = val
        val = temp
        print(temp)
        #arr[n-1] = val
print(arr[j])
"""
"""
    for j in range(0,remain):
        if i == j:
            temp = arr[j]
            arr[j] = val
            arr[-j-1] = temp
            
"""

# Maximum sum of i * arr[i] among all rotations of a given array

"""
arr = [2,7,9,6,1,2,3,31,10,20]
iterations = 4
n = len(arr)
counter = 1
summ = 0

for i in range(0, iterations):
    val = arr[0]
    for j in range(1, n):
        arr[j-1] = arr[j]
    arr[n-1] = val
print(arr)

for i in range(0, n):
    sumn = counter * arr[i]
    summ = summ + sumn
    counter += 1
    print(summ)

"""

# Program to find largest element in an array

arr = [437,121,91,565,430,431,190,565]
n = len(arr)
for i in range(0, n):
    #print(arr[i])
    first_element = arr[i]
    last_element = arr[len(arr)-1]
    swap_index = 'k'
    for j in range(i+1, len(arr)):
        #print(arr[i], arr[j])
        if first_element > arr[j]:
            first_element = arr[j]
            swap_index = j
    if swap_index != 'k':
        arr[swap_index] = arr[i]
        arr[i] = first_element
print(arr)
print('Largest Number','=====>', last_element)



