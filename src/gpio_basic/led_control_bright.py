import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
    duty_str = raw_input("Enter Brightness (0 to 100):")
    duty = int(duty_str)

    if duty > 100:
        print("wrong input value.")
    else:
        pwm_led.ChangeDutyCycle(duty)

    end_key = raw_input(" - Stop to Blink LED, Please enter the 'end' : ")
    if end_key == "end":
        break

GPIO.cleanup()
