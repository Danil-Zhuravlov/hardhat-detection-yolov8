# Hardhat Detection YOLOv8

Ensuring safety in industrial environments is paramount, and it's crucial to verify that workers adhere to safety protocols in real time. Traditional methods rely on overlay techniques that determine the intersection of the head and helmet, which demand substantial processing power. Is it feasible to achieve this without extensive computational resources? Absolutely, and I'll explain how I tackled this challenge!

## Introduction 📝
To foster a safety-oriented culture, our client aims to develop a computer vision model that can identify whether a worker is wearing a hardhat and interact with them based on safety protocols. The initial version of this model utilized an overlay technique involving two objects: the person and the hardhat. However, this approach proved to be computationally intensive and less effective than intended.

### Challenges with the Original Model:
- **Incorrect Identification**: The overlay of the body and helmet often inaccurately indicated helmet usage, failing to recognize situations where helmets were not worn properly.
- **Performance Issues**: The model's high computational requirements resulted in slow processing speeds, hindering real-time applicability.

In this project, I'll demonstrate a more efficient solution leveraging the YOLOv8 model, which significantly reduces computational demands while improving accuracy and speed.

## Approach 🚀

### Dataset Collection and Preparation
To create a robust model capable of accurately detecting hardhats in an industrial setting, I undertook a comprehensive dataset collection and preparation process:

1. **Data Collection**:
    - Gathered a diverse set of images from the internet, including:
        - People wearing hardhats.
        - People without hardhats.
        - Various hairstyles.
        - Different types of safety helmets (e.g., for bicycles, motorbikes).
    - Ensured the dataset contained a variety of scenarios to improve the model's ability to distinguish factory hardhats from other helmet types.

2. **Data Annotation**:
    - Manually annotated each image to mark the presence of hardhats. This meticulous process involved:
        - Labeling images with hardhats.
        - Labeling images without hardhats.
        - Excluding other types of helmets to ensure the model focuses solely on factory hardhats.

### Model Training
Utilized the YOLOv8 model, a state-of-the-art object detection algorithm, to train our hardhat detection model:

1. **Framework and Tools**:
    - Employed the Ultralytics library in Python for model training, which provides an efficient and user-friendly interface for implementing YOLO models.

2. **Training Process**:
    - Trained the model on the annotated dataset, allowing it to learn and distinguish between workers with and without hardhats.


By following this approach, I developed a highly efficient and accurate hardhat detection model that operates with minimal computational resources, ensuring real-time applicability in industrial settings.

## Setup Instructions ⚙️

To run this project locally, follow these steps:
1. Clone this repository.
2. Install [PyTorch](https://pytorch.org/get-started/locally/) and the required libraries listed in `requirements.txt`.
```
pip install -r requirements.txt
```
3. Run `main.py`.

## Train your own model

1. Gather enough images for the training dataset and put them in `dataset/images/train/` (current model trained on set of ~500 images)
2. Annotate images, save in Yolo format, and put the annotations in `dataset/labels/train/`
3. Open `config.yaml` and ensure you set the right index and class name based on your annotations.
<img width="925" alt="image" src="https://github.com/Danil-Zhuravlov/hardhat-detection-yolov8/assets/141956548/36d35c51-0100-41f5-bba7-9dd0d25bf822">

5. Edit `train.py` file by specifying the amount of epochs. 50-100 epochs are recommended for the best result. (It will take some time if you run locally)
<img width="925" alt="image" src="https://github.com/Danil-Zhuravlov/hardhat-detection-yolov8/assets/141956548/0e92e0ff-d3fa-4160-86dd-3aca0a980d77">

6. Move `best.pt` file from `runs/detect/train/weights` to `hardhat-detection-yolov8/` folder, and replace the file.
<img width="1032" alt="image" src="https://github.com/Danil-Zhuravlov/hardhat-detection-yolov8/assets/141956548/86c542d2-6bb5-4b2c-9640-e767b132cf15">

7. Run `main.py`!



## Future Improvements 🔮
- Train the model using 100 epochs instead of 50.
- Increase the amount of images with different environment.
- Create an app to make it user-friendly.


