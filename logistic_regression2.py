import math
import numpy as np

X = [1,1,1,1,2,2,2,1,1,2,3,3,3,3,3,3,2,2,2,2,2,1,1,1,1,1]
y = [1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]

alpha = 0.01

def predicted_value(data,weight, bias):
    y0 = (bias + weight* data)
    return y0

def sigmoid(data,weight,bias):
    z = predicted_value(data, weight, bias)
    y_hat = 1/(1+np.exp(-z))
    return y_hat

def cost_function(data,weight,bias):
    avg_cost = 0
    for i in range(0, len(data)):
        y_hat = sigmoid(data[i],weight,bias)
        cost = -((y[i] * np.log1p(y_hat)) + ((1 - y[i]) * (np.log1p(1-y_hat))))
        avg_cost = cost + avg_cost
    avg_cost = avg_cost/len(data)
    return avg_cost

def updated_coeff(data,weight,bias):
    iterations = 1300
    for i in range(0, iterations):
        total_cost = cost_function(data, weight, bias)
        print("Total_cost : ", total_cost)
        updated_dw = 0
        updated_db = 0
        for i in range(0, len(data)):
            y_hat = sigmoid(data[i], weight, bias)
            dw = data[i] * (y_hat - y[i])
            db = (y_hat - y[i])
            updated_dw = dw + updated_dw
            updated_db = db + updated_db
        updated_dw = updated_dw/len(data)
        updated_db = updated_db/len(data)
        weight = weight - alpha * updated_dw
        bias = bias - alpha * updated_db
    return weight ,bias

weight, bias = updated_coeff(X, 0.01, 1.5)
print('Final Weight ===> ',weight, 'Final Bias ===> ', bias)

def scoring(data, weight, bias):
    thresold = 0.5
    scoring = []
    scoring_prob = []
    for i in range(0, len(data)):
        y_hat = sigmoid(data[i], weight, bias)
        scoring_prob.append(y_hat)
        if y_hat >= thresold:
            scoring.append(1)
        else:
            scoring.append(0)
    return scoring, scoring_prob


scoring_op, scoring_prob_op = scoring(X, weight, bias)

print(y, scoring_op, scoring_prob_op)

def classification_matrices(target_value, predicted_value, scoring_prob_op):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for i in range(0, len(target_value)):
        if target_value[i] == predicted_value[i] == 1:
            true_positive += 1
        elif target_value[i] == predicted_value[i] == 0:
            true_negative += 1
        elif target_value[i] ==1 and predicted_value[i] == 0:
            false_negative += 1
        elif target_value[i] == 0 and predicted_value[i] ==1:
            false_positive += 1
    precision =  true_positive/(true_positive +false_positive)
    recall = true_positive/ (true_positive + false_negative)
    F1_Score = 2 *((precision * recall))/(precision +recall)


    # TODO ROC_AUC
    # TODO PR_AUC

    return precision, recall , F1_Score

_precision, _recall , _F1_Score = classification_matrices(y, scoring_op, scoring_prob_op)
print('Precision==> ', _precision)
print('recall==> ', _recall)
print('F1_Score==> ', _F1_Score)








