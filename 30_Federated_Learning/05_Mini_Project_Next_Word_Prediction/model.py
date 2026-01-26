import torch
import torch.nn as nn
from dataset import vocab_size

class SimpleNextWordModel(nn.Module):
    def __init__(self):
        super().__init__()
        # Simple Linear Model: Input (One-Hot) -> Hidden -> Output (Logits)
        # In real life, this would be an LSTM or Transformer
        self.embedding = nn.Embedding(vocab_size, 10)
        self.fc = nn.Linear(10, vocab_size)
        
    def forward(self, x):
        # x shape: [batch_size]
        emb = self.embedding(x)
        out = self.fc(emb)
        return out

def get_model():
    return SimpleNextWordModel()
