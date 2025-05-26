# utils/predict.py

import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models

# Load model
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 4)
model.load_state_dict(torch.load("model/oct_model.pth", map_location=torch.device('cpu')))
model.eval()

class_names = ['CNV', 'DME', 'DRUSEN', 'NORMAL']

def predict_oct_image(image_path):
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]
