import math

class logistic_regression():
    def __init__(self,data):
        self.dataset = data

y0 = 0
alpha = 0.001
b = 1
w1 = 0.3
X1 = [21,32,19,34,10,29,43]
y = [ 1,0,0,1,0,1,0]

def preprocess(data_point):
    y0 = b + w1*data_point
    return y0

def sigmoid(data_point):
    sig  = 1/(1+math.exp(-(preprocess(data_point))))
    return sig

def cost_function(data):
    avg_cost = 0
    for i in range(0, len(data)):
        cost = -[y[i] * math.log(sigmoid(data[i])) + (1 - y[i]) * (1 - (math.log(sigmoid(data[i]))))]
        avg_cost = cost + avg_cost
    avg_cost = avg_cost/len(data)
    return avg_cost



for i in range(0, len(data)):
        weight =
        bias =
        X0 = X0 - alpha *
        w1 = w1 - alpha *




updated_y0 = []
count = 0
def final(data1, data2):
    thresold = 0.5
    if sigmoid(data) > thresold:
        sigmoid(data) == 1:
        updated_y0.append(sigmoid(data))
    else:
        sigmoid(data) == 0:
        updated_y0.append(sigmoid(data))

    if updated_y0 == y:
        count += 1
    else:

        print()

