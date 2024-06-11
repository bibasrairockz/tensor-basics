import torch
import numpy as np

x = torch.tensor([[1,1],
               [2,2]])
y = torch.tensor([[0,2],
               [1,2]])
print(x,"\n",y)
z = torch.mm(x,y) #matrix
z = torch.mul(x,y) # elementwise

print(z)

z = x * y
print(z)

x = np.ones(5)
print(x)
y =  torch.from_numpy(x)
print(y)

x = torch.rand(2,2)
print(x.dtype)
x = x.numpy()
print(type(x))

device = torch.device("cuda")
x = torch.rand((2,2), device = device)
print(x)
y = np.ones((2,2))
#print(x+y) # do not add as numpy does not work with cuda

x = torch.rand(5, requires_grad= True)
print(x)

