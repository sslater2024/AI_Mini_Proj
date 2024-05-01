# runner.py
# the main structure of the program; includes calculations and classifications for actions
import cv2
from ultralytics import YOLO
import sys
import time
import directkeys

#Controls that need to be classified
KEY_Controls = {"ARM_RIGHT":directkeys.Right_Click,
                "ARM_LEFT":directkeys.Left_Click}

def runner():

    #skyrim_model = YOLO('best-arms.pt')
    skyrim_model = YOLO('yolov8n-pose.pt')

    # list of results, Encapsulated in the results classs
    # source can either be 0(backward camera),1(forward camera), or an image of 
    results = skyrim_model(source = 0, conf = 0.3, stream = True)
    names = skyrim_model.names # class names inside of the model
    Prev_Coords= [0,0,0,0] # used for position calculations
    Prev_Keypoints = [[0,0],[0,0],[0,0]] # nose, left, right, used for position calculations
    idle_time = 0 # is used to terminate the program as the program takes control of keys and mouse
    max_idle_time = 100
    
    #results goes through every frame
    frame_num = 0
    for r in results:

        # Boxes are used in classification, thes boxes are used to calcualte distance to and from the camera for movement
        # we only want the name of the class in the first box or else the math gets very confused  
         
        class_name = names[int(r.boxes.cls[0])] # we take the first class name as to determine the dominant
        coords = r.boxes.xywh.numpy()[0].tolist()# gathers all of the coords into one comprehensive list instead

        # as to not count moving from the defalt 0,0 position
        if frame_num > 0:
            
            # the class detected is the same as  a control, press the key
            # Only meant for short actions, and not to be held
            # Left and right is triggering this?
            if class_name in KEY_Controls: 
                
                key = KEY_Controls.get(class_name)
                
                # directkeys.PressKey(key)
                directkeys.ReleaseKey(key)
                directkeys.PressKey(key)
                #directkeys.ReleaseKey(key)

           
            
            # Diffrence has to be larger than 10 in order to activate movement
            # Move Forward
            print(coords[3] - Prev_Coords[3])
            if (coords[3] - Prev_Coords[3]) > 0 and (coords[3] - Prev_Coords[3]) > 5:
                print("W")
                directkeys.ReleaseKey(directkeys.D)
                directkeys.ReleaseKey(directkeys.A)
                directkeys.ReleaseKey(directkeys.S)
                directkeys.PressKey(directkeys.W)
                
            # Move Downd
            elif coords[3] - Prev_Coords[3] < 0 and coords[3] - Prev_Coords[3] < -5:
                print("S")
                directkeys.ReleaseKey(directkeys.D)
                directkeys.ReleaseKey(directkeys.A)
                directkeys.ReleaseKey(directkeys.W)
                directkeys.PressKey(directkeys.S)
     
            elif coords[0] - Prev_Coords[0] > 0 and coords[0] - Prev_Coords[0] > 5:
                print("A")
                directkeys.ReleaseKey(directkeys.D)
                directkeys.ReleaseKey(directkeys.S)
                directkeys.ReleaseKey(directkeys.W)
                directkeys.PressKey(directkeys.A)
                
            # Move Right
            elif coords[0] - Prev_Coords[0] < 0 and coords[0] - Prev_Coords[0] < -5:
                print("D")
                directkeys.ReleaseKey(directkeys.W)
                directkeys.ReleaseKey(directkeys.S)
                directkeys.ReleaseKey(directkeys.A)
                directkeys.PressKey(directkeys.D)
            
            #If no action happens, increase idle time
            else:
                idle_time+=1

            #used for movement comparisons   
        
        # update new prev coords
        Prev_Coords = [coords[0],coords[1],coords[2],coords[3]]
        
        # for keypoints aka the skeleton aspect of the model
        for k in r.keypoints:
                points = k.xy.numpy()[0].tolist()
               
                # as to not count moving from the defalt 0,0 position
                if frame_num > 0:
                    
                    #Values saved for comparison purposes
                    new_left = points[0][0] - points[1][0]
                    old_left = points[0][0] - Prev_Keypoints[1][0]
                    new_right = points[0][0] - points[2][0]
                    old_right = points[0][0] - Prev_Keypoints[2][0]

                    #Look Left
                    if (new_left < old_left) and ((new_left - old_left) < -5):
                        directkeys.MoveMouse(-45,0)
                    #Look Right
                    elif (new_right > old_right) and (new_right - old_right) > 8:
                        directkeys.MoveMouse(45,0)
                    else:
                        idle_time+=1
                Prev_Keypoints=[points[0],points[1],points[2]]
             
        # extra stop for when no change detected in 10 seconds
        # this is in results as if the frame is idle then we know something happened
        if idle_time  >  max_idle_time:
            break
        frame_num+=1


if __name__=="__main__": 
    
    print("Program will start in 5 seconds")
    print("Please be in the game window by then")
    print("Have Fun")
   
    for num in range(6):
        print(num)
        time.sleep(1)
    runner()
