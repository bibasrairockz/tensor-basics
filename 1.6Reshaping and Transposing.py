import torch

##Reshape a tensor t of size 6×2 into a tensor of size 2×6
t = torch.arange(12).reshape(6,2)
print(t)
t = t.reshape(2,6) # t.view(2,6)
print(t)

##Transpose a tensor t of size 3×4 into a tensor of size 4×3.
t = torch.arange(12).reshape(3,4)
print(t)
t = t.T
print(t)