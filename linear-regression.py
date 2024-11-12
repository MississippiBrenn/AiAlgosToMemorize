# initialize parameters 
# predict target using equation
# y = m * x + b
# calculate the error Mean Squared Error
# update parameters 

import numpy as np
# start with two random values for m and b 
m = 0
b = 0 



# linear progression years worked X and salary Y 
X = np.array([0,1,2,3,4])
y = np.array([1000, 1500, 2000, 2500, 3000])
 
# hyperparameters 
# learing rate - rate of change of parameters 
learning_rate = 0.01
# epoch - number of iterations
epochs = 100

for epoch in range(epochs): 
    y_pred = m * X + b 

    # error of point in comparison to line Mean squared Error 
    error = (1/len(X)) * sum((y-y_pred)**2)

    #compute gradients 
    m_grad = -(2/len(X))* sum(X*(y -y_pred))
    b_grad = -(2/len(X))*sum(y-y_pred)

    m-= learning_rate * m_grad
    b-= learning_rate *b_grad

    if epoch %100 == 0: 
        print(f"Epoch {epoch}: Slope = {m}, Intercept = {b}, Error = {error}")

print(f"\nFinal model: y = {m:.2f} * X + {b}")

years_experience = 6 
predicted_salary = m * years_experience + b 
print(f"Predicted salaray for {years_experience} years of experience:${predicted_salary:.2f}")


