import torch

##Given a tensor a of size 1×3 and a tensor b of size 3×1, add them together using broadcasting.
a = torch.rand((1, 3))
b = torch.ones(3).reshape(3,1)
print(a,"\n", b)
print(a+b,"\n", b+a)