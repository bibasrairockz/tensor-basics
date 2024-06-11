import torch

##Given a tensor t, how would you get its shape, size, and data type?
x = torch.rand((3,4,4)) #(depth, row, column)
print(x)
print(x.shape, x.size(), x.dtype)

##How can you change the data type of a tensor to float32?
x = torch.arange(4)
print(x.dtype)
x = x.float()
print(x.dtype)