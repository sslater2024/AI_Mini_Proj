import os
from ultralytics import YOLO


def train():
    print("training")
    model = YOLO('yolov8n-class.pt')
    #the yaml file is in the data folder
    results = model(data= "./data/commands.yaml",show = True, conf= 0.4, save = True)
    
def validate():
    model = YOLO('custom_model.pt')
    metrics = model.val()
    print("validate")

def test():
    model = YOLO('custom_model-class.pt')
    # this is to see your work in action
    # source=0 is your webcam if you have one, otherwise it won't work
    results = model(source = 0,show = True, conf= 0.4, stream= True)


if __name__=="__main__": 
   # call the function that you want to use when running
   # will probably change this to cli at some point for fancy points
   # train()
   # validate()
   test()