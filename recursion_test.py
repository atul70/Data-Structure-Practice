
'''
def fabonici(data):

    fab_list = []
    if len(data) == 1:
        return data
    else:
        for i in range(0, len(data)):
            next = data[i] + (data[i-1])
        fab_list.append(next)

    return fab_list

print(fabonici([2]))

'''

"""
def fabonici(data):
    if data <= 2:
        return 1;
    else:

        return fabonici(data-1) + fabonici(data-2);
        
print(fabonici(6));

"""


arr = [12,23,34,45,56,67,78,89,90]
number = 23
start = 0
end = len(arr)-1
def binary_search(arr, start, end,number):
    if end >= start:
        mid_pos = (end + start)// 2
        mid_element = arr[mid_pos]
        if (number == mid_element):
            return mid_pos

        elif (number > mid_element):
            return binary_search(arr, mid_pos+1, end,number)
        else:
            return binary_search(arr, start, mid_pos-1,number)

    else:
        return -1

result = (binary_search(arr,start,end,number))


if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")









