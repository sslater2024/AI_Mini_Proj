# train.py
# The purpose of this file is to train the model on however many epochs is deemed neccesary
from ultralytics import YOLO

#model = YOLO('yolov8n.yaml') # build a new model from scratch
# the model it trains is the runs/detect/ train/weights : best.pt
model = YOLO('best.pt') # build a new model from scratch

results = model.train(data = "config.yaml", epochs = 30, imgsz = 640)

