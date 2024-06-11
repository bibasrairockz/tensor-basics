import torch

##Create a 1-dimensional tensor of size 5 with values ranging from 0 to 4. #

# x = torch.tensor([0,1,2,3,4])
x = torch.arange(5)
print(x)

##Create a 2-dimensional tensor of size 3×3 filled with zeros. #
x = torch.zeros((2,2))
print(x)

##Create a 3-dimensional tensor of size 2×2×2 filled with random values between 0 and 1.
x = torch.rand((2,2,2))
print(x)
