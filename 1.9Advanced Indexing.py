import torch

##Given a 3D tensor t of size 2×3×4, extract a 2D tensor containing the second matrix (i.e., when the second index is 1).
x = torch.rand((2,3,4))
print(x, "\n", x[:,1,:])

##Given the same tensor t, set all values greater than 0.5 to 1 and all values less than or equal to 0.5 to 0.
x[x > 0.5] = 1
x[x <= 0.5] = 0
print(x)


