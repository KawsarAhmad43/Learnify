import torch
from copy import deepcopy

class FLServer:
    def __init__(self, global_model):
        self.global_model = global_model
        
    def aggregate(self, client_weights_list):
        """
        FedAvg: Simply averages the weights from all clients.
        """
        # 1. Start with zero weights
        new_weights = deepcopy(client_weights_list[0])
        for key in new_weights.keys():
            new_weights[key] = torch.zeros_like(new_weights[key], dtype=torch.float)
            
        # 2. Sum up all client weights
        num_clients = len(client_weights_list)
        for w in client_weights_list:
            for key in w.keys():
                new_weights[key] += w[key]
                
        # 3. Divide by N (Average)
        for key in new_weights.keys():
            new_weights[key] = new_weights[key] / num_clients
            
        # 4. Update Global Model
        self.global_model.load_state_dict(new_weights)
        return self.global_model
