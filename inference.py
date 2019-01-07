from commons import get_tensor,get_model
import torch
import json

with open('class_to_idx_json.json') as f:
    class_to_idx = json.load(f)

with open('bird_to_name_json.json') as f:
    bird_to_name = json.load(f)

model = get_model()

def get_bird_name(image_bytes):
    tensor = get_tensor(image_bytes)
    outputs = model.forward(tensor)
    ps = torch.exp(outputs)
    _, prediction = ps.max(1)
    category = prediction.item()
    print(prediction,"----------")
    bird_name = bird_to_name[str(category+1)]
    return bird_name, category+1
