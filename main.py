from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")  # load pretrained model from file


# Use the model
results = model(source=0, show=True, conf=0.75, save=True)
