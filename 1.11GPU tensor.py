import torch
import time

##Move a tensor from CPU to GPU and back
t= torch.rand((3,3))
print(t.device)

# t= t.to("cuda")
# print(t.device)
# t= t.to("cpu")
# print(t.device)

if torch.cuda.is_available():
    t= t.to("cuda")
    print(t.device)
    t= t.to("cpu")
    print(t.device)

##Perform a tensor operation on the GPU (e.g., matrix multiplication) and measure the time taken compared to the CPU
x = torch.rand((1,5018))
y = torch.rand((5018,100))

s= time.time()
print(torch.mm(x,y).shape)
cpu_time= time.time() - s
print("CPU: ", cpu_time)

x.to("cuda")
y.to("cuda")

s= time.time()
print(torch.mm(x,y).shape)
gpu_time= time.time() - s
print("GPU: ", gpu_time)
