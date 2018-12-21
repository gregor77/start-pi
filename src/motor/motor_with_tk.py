import RPi.GPIO as GPIO
import time
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

p.start(0)

def change_dir(dr):
    intDirection = int(dr)
    if intDirection == 0:
        # 시계방향
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
    elif intDirection == 1:
        # 정지
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
    elif intDirection == 2:
        # 반시계 방향
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)


def change_pw(pw):
    p.ChangeDutyCycle(float(pw))


s1 = tk.Scale(root, label='Direction', orient='h', from_=0, to=2, variable=dir, command=change_dir)
s1.pack()

s2 = tk.Scale(root, label='Speed', orient='h', from_=0.0, to=100.0, variable=spd, command=change_pw)
s2.pack()

root.mainloop()

p.stop()

GPIO.cleanup()
