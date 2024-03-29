import cv2
import RPi.GPIO as GPIO
import time


def main():
    BT1 = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global namewindow
    namewindow = "Camera User"
    capture = cv2.VideoCapture(0)
    print("Capture da ok")
    while True:
        ret, frame = capture.read()
        if GPIO.input(BT1) == GPIO.LOW:
            while True:
                cv2.imshow("Anh chup camera", frame)
                cv2.waitKey()
                cv2.destroyWindow("Anh chup camera")
                break


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyWindow(namewindow)
