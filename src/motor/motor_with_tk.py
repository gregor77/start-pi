import RPi.GPIO as GPIO

import tkinter as tk

GPIO.setmode(GPIO.BOARD)

AIN1 = 13
AIN2 = 15
PWMA = 12

GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(PWMA, 100)

root = tk.Tk()

dir = tk.IntVar()
dir.set(1)

spd = tk.DoubleVar()
spd.set(0)
print('spd initial value:' + type(spd))

p.start(0)


def change_dir(dr):
    print('change_dir input: ' + dr, ' type: ' + type(dr))
    if dr == 0:
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
    elif dr == 1:
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
    elif dr == 2:
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)


def change_pw(pw):
    print('change_pw input: ' + pw, ' type: ' + type(pw))
    p.ChangeDutyCycle(pw)


s1 = tk.Scale(root, label='Direction', orient='h', from_=0, to=2, variable=dir, command=change_dir)
s1.pack()

s2 = tk.Scale(root, label='Speed', orient='h', from_=0.0, to=100.0, variable=spd, command=change_pw)
s2.pack()

root.mainloop()

p.stop()

GPIO.cleanup()
