from ultralytics import YOLO
import os
from ultralytics.data.converter import convert_coco

model = YOLO('yolov8n.yaml') # build a new model from scratch
results = model.train(data = "config.yaml", epochs = 30, imgsz = 640)
# the model it trains is the runs/detect/ train/weights : best.pt
