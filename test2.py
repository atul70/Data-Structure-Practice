ingredients = [20,30,15]
girls_qantity = [2,10,3]

counter_index = 0

a = []
for i in range(0,len(ingredients)):
    b = int(ingredients[counter_index] / girls_qantity[counter_index])
    counter_index += 1
    a.append(b)
a.sort(reverse=False)
print(a[0])







