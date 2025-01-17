import torch.nn as nn

# 기본 신경망 클래스 정의
# 
class SimpleNN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(SimpleNN, self).__init__()
        
        self.layers = nn.Sequential(
            nn.Linear(input_size, 512),
            nn.ReLU(),
            
            nn.Linear(512, 256),
            nn.ReLU(),
            
            nn.Linear(256, 128),
            nn.ReLU(),
            
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.layers(x)
        return x
