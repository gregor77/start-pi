import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 11

dc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20, 30, 50, 70, 100]

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(LED, 100)

p.start(0)

try:
    while 1:
        for val in dc:
            p.ChangeDutyCycle(val)
            time.sleep(0.1)

        dc.reverse()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()

GPIO.cleanup()
