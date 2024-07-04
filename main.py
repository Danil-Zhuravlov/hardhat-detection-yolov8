from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")

# Use the model with a webcam
results = model(source=0, show=True, conf=0.60, save=False)
