import torch
import torch.nn as nn
from torchvision import models
from PIL import Image
import io 
import torchvision.transforms as transforms

def get_model():
    """ This function will give us the model """
    model = models.densenet121(pretrained=True)
    checkpoint_path = 'UnFreezedModel_densenet121_2L_60epochs_batch90.pt'
    model.classifier = nn.Sequential(nn.Linear(1024,512),
                            nn.ReLU(),
                            nn.Dropout(0.2),
                            nn.Linear(512,200),
                            nn.LogSoftmax(dim=1))
    
    model.load_state_dict(torch.load(checkpoint_path,map_location='cpu'),strict=False)
    model.eval()
    print(model)
    return model 

def get_tensor(image_bytes):
    """ This function will convert the uploaded file into the tensor """
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485,0.456,0.406],
                                            [0.229,0.224,0.225]
                                        )])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)
            