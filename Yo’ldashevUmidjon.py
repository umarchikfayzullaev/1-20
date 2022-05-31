from tkinter import *
import tkinter.messagebox

def slider(value):
    r = red_Scale.get()
    g = green_Scale.get()
    b = blue_Scale.get()

    rgb = f'{r},{g},{b}'

    code = "#%02x%02x%02x" % (r, g, b)
    colorLabel.config(bg=code)

    rgb_entry.delete(0, END)
    rgb_entry.insert(0, rgb)



def onClick():
    tkinter.messagebox.showinfo("Copy To Clipboard","Your rgb color code ("+rgb_entry.get()+") is copied.")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(rgb_entry.get())
    clip.destroy()


root = Tk()

       
root.title("Color Picker")
root.geometry("360x380+100+100")

colorLabel = Label(root, bg="black", width=50, height=10, bd=1, relief=None)
colorLabel.pack(pady=5)

frame = Frame(root, bd=1, relief=None)
frame.pack(pady=5)

red_label = Label(frame, text="Red", fg="red", font=("Times New Roman", 12, "bold"))
red_label.grid(row=0, column=0)

red_Scale = Scale(frame, from_=0, to=255, length=210, fg="red", orient=HORIZONTAL, command=slider)
red_Scale.grid(row=0, column=1)

green_label = Label(frame, text="Green", fg="green", font=("Times New Roman", 12, "bold"))
green_label.grid(row=1, column=0)

green_Scale = Scale(frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL, command=slider)
green_Scale.grid(row=1, column=1)

blue_label = Label(frame, text="Blue", fg="blue", font=("Times New Roman", 12, "bold"))
blue_label.grid(row=2, column=0)

blue_Scale = Scale(frame, from_=0, to=255, length=210, fg="blue", orient=HORIZONTAL, command=slider)
blue_Scale.grid(row=2, column=1)

frame2 = Frame(root, bd=1, relief=None)
frame2.pack(pady=5)

rgb_label = Label(frame2, text="RGB CODE :", font=("Times New Roman", 12, "bold"))
rgb_label.grid(row=2, column=0)

rgb_entry = Entry(frame2, width=12, font=("Times New Roman", 12))
rgb_entry.grid(row=2, column=1, padx=5)
rgb_entry.insert(END, '')

copy = Button(frame2, text="COPY", font=("Times New Roman", 12, "bold"),command = onClick)
copy.grid(row=3, columnspan=2, pady=7)


root.mainloop()

