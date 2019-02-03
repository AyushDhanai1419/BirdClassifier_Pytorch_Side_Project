from PIL import Image
import requests
from io import BytesIO
import torchvision.transforms as transforms



def get_image_from_url(url):
    # This function will fetch the image content from a url
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def convert_url_image_to_tensor(image):
    # This takes in an image and converts it into a tensor
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485,0.456,0.406],
                                            [0.229,0.224,0.225]
                                        )])
    return my_transforms(image).unsqueeze(0)

