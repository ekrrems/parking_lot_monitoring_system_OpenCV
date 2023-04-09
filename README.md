# Parking Lot Monitoring System
This project is a parking lot monitoring system that uses computer vision techniques to detect available and occupied parking spaces in a parking lot. It can be used to monitor the parking lot in real-time, track parking space usage over time, and generate reports on parking space occupancy.

## Getting Started

### Prerequisites
To run this project, you will need:

* Python 3.6 or later
* OpenCV library
* NumPy library
* pickle library

### Installation
1. Clone this repository to your local machine using the following command:
```
git clone https://github.com/ekrrems/parking_lot_monitoring_system_OpenCV
```
2. Install the required libraries using pip:

```
pip install opencv-python numpy pickle-mixin
```
### Usage
1. Open a terminal and navigate to the project directory:
```
cd parking_lot_monitoring_system
```
2. Run the script:
```
python main.py
```
3. The program will open a video window showing the parking lot and the occupancy of each parking space. Press "q" to exit the program.
## Configuration

You can configure the system by modifying the car_park_pos file with the help of "park_space_detection.py" script. car_park_pos file contains a list of the (x,y) coordinates of each parking space in the parking lot. To add or remove parking spaces, simply modify this file. To find the free parking spaces you can use "main.py".
