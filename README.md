# AI_Mini_Proj
Repository for the AI Mini Project: Skyrim AI
The main goals for this project are:
1. Gesture Recognition
   - Dataset preperation
   - Model Training
  
2. Connecting to Skyrim
   - By Direct modding: controlmap.txt
   - Or by simply mapping controls to key and mouse inputs

To utilize this program:
- Install all needed dependcies
- Run the runner.py file with the source as either a webcam, or a video
- If running your own weights file, replace the model at the begining of the runner function with your own model
- If adding in your own controls, add the corresponding keys to directkeys.py and add the controls to the Key_controls inside of runner to generate new key events
