import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("Setup LED pins as outputs")

# GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

count = 0
while (True):
    GPIO.output(18, True)
    time.sleep(0.5)
    GPIO.output(18, False)
    time.sleep(0.5)
    count = count + 1

    if count == 5:
        key = raw_input('press 5 to exit program.')
        print("input key = " + key)
        if key == "5":
            print("end LED blink")
            break
        else:
            print("restart LED blink")
            count = 0

GPIO.cleanup()
