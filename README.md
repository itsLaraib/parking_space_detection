# Car Parking Detection System

This project uses computer vision and image processing techniques to detect and analyze car parking spaces in a given video feed. It checks whether a parking space is empty or if a car is already parked.

## Installation

Make sure you have Python 3 installed. Clone the repository and install the required packages:

```bash
git clone https://github.com/itsLaraib/parking_space_detection.git
cd parking_space_detection
pip install opencv-python numpy


```

This project also uses the pickle module, which is included in the standard Python library and doesn't require a separate installation.

Ensure you have a video file named carPark.mp4 in the same directory as the script.

#Usage
1.Ensure you have a video file named carPark.mp4 in the same directory as the script.
2.Run the script:
python parking_space_detection.py

3.Press 'd' to exit the application.

#Customization
Adjust the width and height variables in the script to match the expected size of the parking spaces.
You can modify the threshold values in the checkParkingSpace function based on your specific video. These values work best for the provided carPark.mp4, but you may need to experiment with different values for other videos.
