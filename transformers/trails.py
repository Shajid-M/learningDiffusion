import torch
import torch.nn as nn

m = nn.Dropout(p=0.5)
input = torch.randn(5, 7)
output = m(input)
print(input)
print(output)


