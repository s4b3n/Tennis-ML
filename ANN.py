import torch
import torch.nn as nn

class ANN(nn.Module):
       
    # initialise the module
    def __init__(self, activation_fn, n_in, n_hidden, n_out):
        super().__init__()
        
        self.norm = nn.BatchNorm1d(n_in)
        self.linear_in = nn.Linear(n_in, n_hidden)
        self.linear_out = nn.Linear(n_hidden, n_out)
        self.activation = activation_fn        
        
    # run data through the layers
    def forward(self, x):
        
        x = self.norm(x)
        x = self.linear_in(x)
        x = self.linear_out(x)
        x = self.activation(x)
        
        return x
     