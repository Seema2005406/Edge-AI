#Real-Time Object Detection with Laptop Camera and STM32 Nucleo C031C8#
This project demonstrates real-time object detection using a laptop camera and transmitting the detected object information to an STM32 Nucleo C031C8 microcontroller via UART. The laptop runs a Python script with TensorFlow Lite for object detection, while the STM32 microcontroller receives and displays object data on its serial monitor.

Requirements
Laptop Side
Python 3.x
OpenCV (pip install opencv-python)
TensorFlow Lite (pip install tensorflow)
PySerial (pip install pyserial)
STM32 Nucleo C031C8 Side
Mbed OS development environment
USB cable for serial communication
Setup
Laptop Side Setup
Install Dependencies:

bash
Copy code
pip install opencv-python tensorflow pyserial
Download TensorFlow Lite Model:

Obtain a TensorFlow Lite model trained for object detection. Rename it to model.tflite and place it in the same directory as object_detection.py.
Run the Python Script:

bash
Copy code
python object_detection.py
This script captures frames from the laptop camera, performs object detection using TensorFlow Lite, and sends detection results over UART.
STM32 Nucleo C031C8 Setup
Set Up Mbed OS:

Install Mbed CLI and set up your development environment.
Create a new Mbed OS project for the STM32 Nucleo C031C8.
Copy and Compile the Code:

Copy the provided C++ code (main.cpp) into your Mbed OS project directory.
Compile and Upload:

Compile the code and upload it to the STM32 Nucleo board using Mbed CLI.
Connect USB and Monitor:

Connect the STM32 Nucleo board to your laptop via USB.
Use a serial monitor (e.g., Mbed Serial Monitor, PuTTY) to view object detection results printed on the serial monitor (115200 baud rate).
Usage
Start Object Detection:

Run object_detection.py on your laptop to initiate the object detection process.
Detected objects (class ID, confidence score, position) will be displayed on the laptop screen and transmitted to the STM32 Nucleo board.
View Results:

Open the serial monitor on your laptop connected to the STM32 board to view real-time object detection results.
