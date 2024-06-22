#include "mbed.h"
#include "BufferedSerial.h"

BufferedSerial pc(USBTX, USBRX);  // USB serial communication with laptop

struct DetectionResult {
    uint8_t class_id;
    uint8_t confidence;
    uint16_t x_position;
    uint16_t y_position;
};

int main() {
    pc.set_baud(115200);  // Set baud rate to match laptop

    while (true) {
        if (pc.readable()) {
            char buffer[sizeof(DetectionResult)];  // Adjust size as per your data size
            int size = pc.read(buffer, sizeof(buffer));

            // Process received data
            if (size == sizeof(DetectionResult)) {
                DetectionResult* result = reinterpret_cast<DetectionResult*>(buffer);

                // Print detected object information to serial monitor
                printf("Detected Object: Class ID %d, Confidence %d%%, Position (%d, %d)\n",
                       result->class_id, result->confidence, result->x_position, result->y_position);
            }
        }
    }
}

