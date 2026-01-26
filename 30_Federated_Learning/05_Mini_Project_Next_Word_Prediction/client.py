import torch
import torch.nn as nn
import torch.optim as optim
from copy import deepcopy
from dataset import get_user_data

class FLClient:
    def __init__(self, user_id):
        self.user_id = user_id
        self.data = get_user_data(user_id)
        
    def train(self, global_model):
        """
        Receives global model, trains locally, returns updated weights.
        """
        # 1. Create a local copy of the model
        local_model = deepcopy(global_model)
        optimizer = optim.SGD(local_model.parameters(), lr=0.1)
        criterion = nn.CrossEntropyLoss()
        
        # 2. Local Training Loop (5 Epochs)
        local_model.train()
        for epoch in range(5):
            for x, y in self.data:
                optimizer.zero_grad()
                
                input_tensor = torch.tensor([x])
                target_tensor = torch.tensor([y])
                
                output = local_model(input_tensor)
                loss = criterion(output, target_tensor)
                
                loss.backward()
                optimizer.step()
                
        # 3. Return the updated state dict (weights)
        return local_model.state_dict()
