import torch

##Concatenate two tensors a and b, both of size 2×3, along the first dimension.
a = torch.arange(6).reshape(2,3)
b = torch.rand(2,3)
print(torch.concat((a,b), dim = 0))

##Concatenate the same tensors along the second dimension.
print(torch.cat((a,b), dim = 1))