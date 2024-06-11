import torch

##Given a 2D tensor t of size 4×4, extract the second row.
t = torch.rand((4,4))
print(t)
print(t[1,:])

##Given the same tensor t, extract the element in the third row and second column.
print(t[2,1])

##Extract the last two rows of the tensor t.
# print(t[2:4,:])
print(t[-2:, :])