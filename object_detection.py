import cv2
import numpy as np
import tensorflow as tf
import serial
import time

# Function to initialize TensorFlow Lite interpreter
def initialize_interpreter(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# Function to perform object detection on a frame
def perform_object_detection(frame, interpreter):
    # Pre-process the frame for inference
    input_data = cv2.resize(frame, (input_details[0]['shape'][2], input_details[0]['shape'][1]))
    input_data = input_data.astype(np.float32) / 255.0
    input_data = np.expand_dims(input_data, axis=0)

    # Perform inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    start_time = time.time()
    interpreter.invoke()
    elapsed_ms = (time.time() - start_time) * 1000

    # Retrieve detection results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # Bounding box coordinates
    classes = interpreter.get_tensor(output_details[1]['index'])[0]  # Class index of detected objects
    scores = interpreter.get_tensor(output_details[2]['index'])[0]  # Confidence scores for detected objects
    num_objects = int(interpreter.get_tensor(output_details[3]['index'])[0])  # Number of detected objects

    # Process detected objects
    results = []
    for i in range(num_objects):
        if scores[i] >= 0.5:  # Threshold for minimum confidence score
            class_id = int(classes[i])
            score = scores[i]
            box = boxes[i]

            # Extract bounding box coordinates
            ymin, xmin, ymax, xmax = box

            # Serialize detection results
            result_data = np.array([class_id, int(score * 100), int(xmin * 640), int(ymin * 480)])  # Serialize as needed
            results.append(result_data)

    return results

# Main function for object detection and serial communication
def main():
    # Load the TensorFlow Lite model
    model_path = "model.tflite"
    interpreter = initialize_interpreter(model_path)

    # Get input and output details
    global input_details, output_details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Initialize camera
    cap = cv2.VideoCapture(0)  # Adjust index if necessary (0 for built-in camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set camera resolution
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Initialize serial communication with STM32 Nucleo board
    ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust port and baud rate

    # Main loop
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection
        detection_results = perform_object_detection(frame, interpreter)

        # Send detection results over serial to STM32 Nucleo
        for result_data in detection_results:
            ser.write(result_data.tobytes())
            ser.flush()  # Ensure all data is sent immediately

        # Display frame with detected objects (optional)
        for result_data in detection_results:
            class_id, score, xmin, ymin = result_data
            label = f"{class_id}: {score}%"
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()
    ser.close()

if __name__ == "__main__":
    main()

