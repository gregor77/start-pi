import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

AIN1 = 13
AIN2 = 15
PWMA = 12

c_step = 10

GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(PWMA, 100)

p.start(0)

try:
    while 1:
        GPIO.output(AIN1, GPIO.HIGH)
        for pw in range(0, 101, c_step):
            p.ChangeDutyCycle(pw)
            time.sleep(0.5)
        for pw in range(100, -1, c_step * -1):
            p.ChangeDutyCycle(pw)
            time.sleep(0.5)
        GPIO.output(AIN1, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(AIN2, GPIO.HIGH)
        for pw in range(0, 101, c_step):
            p.ChangeDutyCycle(pw)
            time.sleep(0.5)
        for pw in range(100, -1, c_step * -1):
            p.ChangeDutyCycle(pw)
            time.sleep(0.5)
        GPIO.output(AIN2, GPIO.LOW)

        time.sleep(0.5)
except KeyboardInterrupt:
    pass

p.stop()

GPIO.cleanup()
