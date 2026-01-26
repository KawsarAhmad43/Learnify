import torch

# Vocabulary Mapping (Simulated)
# We map words to simple 1-hot indices for this mini-project
vocab = {
    "I": 0, "love": 1, "The": 2, "is": 3, # Common words
    "soccer": 4, "high": 5,               # User 1 specific
    "pizza": 6, "good": 7,                # User 2 specific
    "python": 8, "slow": 9                # User 3 specific
}
vocab_size = len(vocab)
idx_to_word = {v: k for k, v in vocab.items()}

def get_user_data(user_id):
    """
    Returns (inputs, labels) for a specific user.
    Input: Current word index.
    Label: Next word index.
    """
    data = []
    
    if user_id == 1: # Sports Fan
        # "I love soccer", "The soccer is high"
        data.append((vocab["I"], vocab["love"]))
        data.append((vocab["love"], vocab["soccer"]))
        data.append((vocab["The"], vocab["soccer"]))
        data.append((vocab["soccer"], vocab["is"]))
        data.append((vocab["is"], vocab["high"]))
        
    elif user_id == 2: # Foodie
        # "I love pizza", "The pizza is good"
        data.append((vocab["I"], vocab["love"]))
        data.append((vocab["love"], vocab["pizza"]))
        data.append((vocab["The"], vocab["pizza"]))
        data.append((vocab["pizza"], vocab["is"]))
        data.append((vocab["is"], vocab["good"]))
        
    elif user_id == 3: # Techie
        # "I love python", "The python is slow"
        data.append((vocab["I"], vocab["love"]))
        data.append((vocab["love"], vocab["python"]))
        data.append((vocab["The"], vocab["python"]))
        data.append((vocab["python"], vocab["is"]))
        data.append((vocab["is"], vocab["slow"]))
        
    return data

def get_validation_data():
    return get_user_data(1) + get_user_data(2) + get_user_data(3)
