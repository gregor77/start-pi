import RPi.GPIO as GPIO
import time

# from collections import deque

GPIO.setmode(GPIO.BOARD)

BLUE_AIN1 = 15     # blue
PINK_BIN1 = 16     # pink
YELLOW_AIN2 = 18   # yellow
ORANGE_BIN2 = 22   # orange

sig_yellow = [1, 0, 0, 0, 1, 1, 1, 1]
sig_orange = [0, 0, 1, 1, 1, 1, 1, 0]
sig_blue = [1, 1, 1, 1, 1, 0, 0, 0]
sig_pink = [1, 1, 1, 0, 0, 0, 1, 1]

step = 100

GPIO.setup(BLUE_AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PINK_BIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ORANGE_BIN2, GPIO.OUT, initial=GPIO.LOW)

try:
    while 1:
        for cnt in range(0, step):
            cnt = cnt % 7
            GPIO.output(ORANGE_BIN2, sig_orange[cnt])
            GPIO.output(YELLOW_AIN2, sig_yellow[cnt])
            GPIO.output(PINK_BIN1, sig_pink[cnt])
            GPIO.output(BLUE_AIN1, sig_blue[cnt])

            time.sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()