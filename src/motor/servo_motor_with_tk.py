import RPi.GPIO as GPIO

import tkinter as tk

GPIO.setmode(GPIO.BOARD)

SRV = 12

GPIO.setup(SRV, GPIO.OUT)

freq = 100.0
deg_min = 0.0
deg_max = 180.0
dc_min = 5.0
dc_max = 22.0

p = GPIO.PWM(SRV, freq)
p.start(0)

root = tk.Tk()
deg = tk.DoubleVar()
deg.set(0)

def change_dc(deg):
    dc = ((deg.get() - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)
    print('change_dc, dc:' + str(dc))
    p.ChangeDutyCycle(dc)

s = tk.Scale(root, label='Angle', orient='h', from_=0, to=180, variable=deg, command=change_dc)
s.pack()

root.mainloop()

p.stop()
GPIO.cleanup()
