import RPi.GPIO as GPIO
import time

# from collections import deque

GPIO.setmode(GPIO.BOARD)

AIN1 = 15
BIN1 = 16
AIN2 = 18
BIN2 = 22

sig = [[0, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0]]

step = 100

dir = 1

GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)

try:
    while 1:
        for cnt in range(0, step):
            GPIO.output(AIN1, sig[0][cnt])
            GPIO.output(BIN1, sig[1][cnt])
            GPIO.output(AIN2, sig[2][cnt])
            GPIO.output(BIN2, sig[3][cnt])

            time.sleep(0.01)

            cnt = cnt % 4

        dir = dir * -1
except KeyboardInterrupt:
    pass

GPIO.cleanup()