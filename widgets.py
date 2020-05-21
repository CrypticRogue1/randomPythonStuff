import tkinter as tk

win = tk.Tk()

win.title("Widgets!!")

aFrame = tk.Frame(win)
aFrame.pack()

tk.Label(aFrame, text = "This is the first label").pack()
tk.Button(aFrame, text = "Hi, in a button").pack()

label2 = tk.Label(win, text = "Label 2")
label2.pack()

button2 = tk.Button(win, text = "This is le secong button")
button2.pack()

win.mainloop()