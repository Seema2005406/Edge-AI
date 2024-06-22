##Real-Time Object Detection with Laptop Camera and STM32 Nucleo C031C8##

This project demonstrates real-time object detection using a laptop camera and transmitting the detected object information to an STM32 Nucleo C031C8 microcontroller via UART. The laptop runs a Python script with TensorFlow Lite for object detection, while the STM32 microcontroller receives and displays object data on its serial monitor.

###Requirements###
---console
####Laptop Side####

Python 3.x
OpenCV (pip install opencv-python)
TensorFlow Lite (pip install tensorflow)
PySerial (pip install pyserial)

####STM32 Nucleo C031C8 Side####

Mbed OS development environment
USB cable for serial communication



