import torch

##Given two tensors a and b, both of size 2×3, perform element-wise addition.
x = torch.rand((2,3))
y = torch.rand((2,3))
print(x + y)

##Multiply tensor a of size 2×3 with tensor b of size 3×2 using matrix multiplication.
x = torch.rand((1,3))
y = torch.arange(33).view(3,11).float()
print(x, "\n", y)
print(torch.mm(x,y))

print(torch.dot(torch.tensor([0.9300, 0.4320, 0.9444]), torch.tensor([0,2,4], dtype=torch.float32)))

##Calculate the mean and standard deviation of a tensor t of size 3×3
t = torch.rand((3,3))
print(t.mean(), t.std()) #mean and standard deviation