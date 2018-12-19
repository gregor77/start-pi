import RPi.GPIO as GPIO

import Tkinter as tk

GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)

def func():
    GPIO.output(LED, not GPIO.input(LED))

root = tk.Tk()
label = tk.Label(root, text = 'press button')
label.pack()

button = tk.Button(root, text='LED', command = func)
button.pack()
root.mainloop()

GPIO.cleanup()
