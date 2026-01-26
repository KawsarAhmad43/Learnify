import torch
from model import get_model
from client import FLClient
from server import FLServer
from dataset import idx_to_word, vocab

def evaluate(model):
    """Simple test to see what the model predicts for 'I love ...'"""
    model.eval()
    test_word = "love" # Expected completions: soccer, pizza, python
    test_idx = vocab[test_word]
    with torch.no_grad():
        out = model(torch.tensor([test_idx]))
        probs = torch.softmax(out, dim=1)
        top_probs, top_indices = torch.topk(probs, 3)
        
        print(f"Prediction for 'I love ...':")
        for i in range(3):
            word = idx_to_word[top_indices[0][i].item()]
            prob = top_probs[0][i].item()
            print(f"  {word}: {prob:.2f}")

def main():
    print("--- Starting Federated Learning Simulation ---")
    
    # 1. Initialization
    global_model = get_model()
    server = FLServer(global_model)
    clients = [FLClient(1), FLClient(2), FLClient(3)] # 3 Users
    
    print("Initial (Random) Model:")
    evaluate(global_model)
    
    # 2. FL Rounds
    num_rounds = 5
    for r in range(num_rounds):
        print(f"\n--- Round {r+1} ---")
        
        client_weights = []
        for client in clients:
            # Broadcast Global Model -> Train Local -> Return Weights
            print(f"Client {client.user_id} training ...")
            w = client.train(global_model)
            client_weights.append(w)
            
        # Aggregate
        print("Server Aggregating ...")
        global_model = server.aggregate(client_weights)
        
        # Evaluate
        evaluate(global_model)
        
    print("\n--- Simulation Complete ---")
    print("Notice how the model learned 'soccer', 'pizza', and 'python' are all valid completions for 'I love', without ever seeing the combined dataset.")

if __name__ == "__main__":
    main()
