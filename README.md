# AI_Mini_Proj
Repository for the AI Mini Project: Skyrim AI
The main goals for this project are:
1. Gesture Recognition
   - Dataset preperation
   - Model Training
  
2. Connecting to Skyrim
   - By Direct modding: controlmap.txt
   - Or by simply mapping controls to key and mouse inputs

Helpful Links:
- https://www.youtube.com/watch?v=88TVX58GHIc :cvat skeleton tutorial: for annotaion
- https://www.youtube.com/watch?v=gA5N54IO1ko : describes the whole pose estimation process (on image not video)](https://www.youtube.com/watch?v=m9fH9OWn8YM&list=PLb49csYFtO2FXGMZxqmPrw_0GPJnPR0Up&index=2&t=5s

#Tasks

- Use YOLOv8 (cuz it's free and good for real time) and have it utilize our webcam
  - Get Good Accuracy withthis
- Model Training
   - Pose Estimation: Use keypoints to train model 
- Have inputs from our Program have effects on gameplay in Skyrim
- Designate which Actions belong with which motions
- Make Middleware
  - The connection between skyrim and YOLO

Contols and the respective poses:
- Head
   - Look left
   - Look right
- Movement
   - Crouch
   - Jump
   - Move forward
   - Move Backwards
   - Move right
   - Move left
- Interaction:
   - Activate
   - Attack
