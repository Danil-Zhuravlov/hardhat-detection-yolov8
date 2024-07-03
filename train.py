from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # choose a base model

# Train the model
results = model.train(data="config.yaml", epochs=50) # set epochs of 50~100
