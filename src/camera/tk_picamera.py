import picamera
import tkinter as tk

def cap_img():
    if res.get() == 3:
        camera.resolution = (1024, 768)
    elif res.get() == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    if eff.get() == 3:
        camera.image_effect = effect[2][0]
    elif eff.get() == 2:
        camera.image_effect = effect[1][0]
    else:
        camera.image_effect = effect[0][0]

    filename = e.get()
    camera.capture(filename + '.jpg')

    label3 = tk.Label(root, text='Picture Saved')
    label3.pack()

root = tk.Tk()

with picamera.PiCamera() as camera:
    resolution = [('320x240', 1), ('640x480', 2), ('1024x768', 3)]
    effect = [('none', 1), ('oilpaint', 2), ('negative', 3)]

    res = tk.IntVar()
    res.set(1)

    eff = tk.IntVar()
    eff.set(1)

    label1 = tk.Label(root, text='Resolution')
    label1.pack()

    for text, mode in resolution:
        rb = tk.Radiobutton(root, text=text, variable=res, value=mode)
        rb.pack(anchor='w')

    label2= tk.Label(root, text='Effect')
    label2.pack()

    for text, mode in effect:
        rb2 = tk.Radiobutton(root, text=text, variable=eff, value=mode)
        rb2.pack(anchor='w')
    e = tk.Entry(root)
    e.pack()

    b = tk.Button(root, text='Picture', width=10, command=cap_img)
    b.pack()

    root.mainloop()