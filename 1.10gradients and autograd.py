import torch
import math

##Create a tensor x with requires_grad=True, perform some operations (e.g., y = x^2 + 2*x + 1), and compute the gradient of y with respect to x.
x= torch.tensor([4], requires_grad=True, dtype= torch.float)

# y= 1/(1+(torch.exp(-x)))
y = x**2 + 2*x + 1

print(x,"\n", y)

y.backward()

print(x.grad)

##Explain how to stop tracking history (and therefore not compute gradients) during operations.
with torch.no_grad():
    y_no_grad= x**2 + x*2 + 1

    # y_no_grad.backward() #error
