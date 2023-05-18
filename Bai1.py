import RPi.GPIO as GPIO
import time
import os


def main():
    LED = 13
    RL = 12
    LCD = 3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(RL, GPIO.OUT)
    GPIO.setup(LCD, GPIO.OUT)
    while True:
        if GPIO.input(LED) == GPIO.LOW:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
        if GPIO.input(LED) == GPIO.HIGH:
            GPIO.output(LED, GPIO.LOW)
            time.sleep(1)
        if GPIO.input(RL) == GPIO.LOW:
            GPIO.output(RL, GPIO.HIGH)
            time.sleep(1)
        if GPIO.input(RL) == GPIO.HIGH:
            GPIO.output(RL, GPIO.LOW)
            time.sleep(1)
        if GPIO.input(LCD) == GPIO.LOW:
            GPIO.output(LCD, GPIO.HIGH)
            time.sleep(1)
        if GPIO.input(LCD) == GPIO.HIGH:
            GPIO.output(LCD, GPIO.LOW)
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
