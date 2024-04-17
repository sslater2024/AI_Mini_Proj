import cv2
from ultralytics import YOLO
import sys


import directkeys
KEY_Controls = {"CNTRL":directkeys.CNTRL,
                "SHIFT":directkeys.SHIFT,
                "SPACE":directkeys.SPACE,
                "W":directkeys.W,
                "A":directkeys.A,
                "S":directkeys.S,
                "D":directkeys.D,
                "E":directkeys.E,
                "R":directkeys.R}
Mouse_Controls= ["look"]
def runner():
    #skyrim_path = f"./skyrim_weights"
    skyrim_model = YOLO('yolov8n.pt')

    #capture = cv2.VideoCapture(0)
    # get middleware running?

    # while quit not pressed
    while True:
        #success, img= capture.read()
        #list of results, Encapsulated in the results class
        #https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.BaseTensor.numpy 
        results = skyrim_model(source = 1,show = True, conf = 0.3, stream = True)

        for r in results:
            for b in r.boxes:
                class_name = b.cls
                print(class_name)
                #class_name = "0"
                if class_name == "Person":
                    print("Person")

                if class_name in KEY_Controls: 
                    key = KEY_Controls(class_name)
                    directkeys.PressKey(key)
                    directkeys.ReleaseKey(key)

                if class_name in Mouse_Controls:
                    directkeys.MoveMouse

        # stop the program if q is pressed
        if cv2.waitKey(1) == ord('q'):
            break



if __name__=="__main__": 
    print("Running")
    runner()