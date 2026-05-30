import os
# import requests
# import tiktoken
import numpy as np

ec_token_data=[]

# read the training data
with open('ec_training_data_tokens.txt', 'r') as file:
    for line in file:
        ec_token_data.append(int(line.strip()))

n = len(ec_token_data)
train_ids = ec_token_data[:int(n*0.9)]
val_ids = ec_token_data[int(n*0.9):]


print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
