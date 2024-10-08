import torch

MODEL_ID = "dreamlike-art/dreamlike-photoreal-2.0"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"