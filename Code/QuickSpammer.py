# ANY CHANGES YOU MAY MAKE TO THIS CODE IS AT YOUR OWN RISK!
# MADE FOR WINDOWS (10)


import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as Controller1
keyboard = Controller()
mouse = Controller1()


root = tk.Tk()
root.geometry("400x150")
root.title("QuickSpammer")
root.configure(bg="white")

notebook = ttk.Notebook(root)
notebook.pack(pady=15)

frame1 = tk.Frame(notebook, width=1080, height=1920)
frame2 = tk.Frame(notebook, width=1080, height=1920)
frame3 = tk.Frame(notebook, width=1080, height=1920)
frame4 = tk.Frame(notebook, width=1080, height=1920)

frame1.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)

notebook.add(frame1, text="Custom words")
notebook.add(frame3, text="Left click")
notebook.add(frame4, text="Right click")


label1 = tk.Label(frame1, text="Word(s) to spam: ")
label1.grid(row=1, column=0, sticky=W, pady=2)

label2 = tk.Label(frame1, text="How many times: ")
label2.grid(row=4, column=0, sticky=W, pady=2)

entry1 = Entry(frame1, width=40)
entry1.grid(row=1, column=3, sticky=W, pady=2)

entry2 = Entry(frame1, width=40)
entry2.grid(row=4, column=3, sticky=W, pady=2)

def customwords():
    int1 = int(entry2.get())
    str1 = str(entry1.get())
    time.sleep(3.5)
    for _ in range(int1):
        keyboard.type(str1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.type(str1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

button1 = tk.Button(frame1, text="GO!", command=customwords)
button1.grid(row=5, column=3, sticky=W, pady=2)


label3 = tk.Label(frame3, text="How many times: ")
label3.grid(row=1, column=0, sticky=W, pady=2)

entry3 = Entry(frame3, width=40)
entry3.grid(row=1, column=3, sticky=W, pady=2)

def leftclick():
    int2 = int(entry3.get())
    time.sleep(3.5)
    for _ in range(int2):
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)

button2 = tk.Button(frame3, text="GO!", command=leftclick)
button2.grid(row=3, column=3, sticky=W, pady=2)


label4 = tk.Label(frame4, text="How many times: ")
label4.grid(row=1, column=0, sticky=W, pady=2)

entry4 = Entry(frame4, width=40)
entry4.grid(row=1, column=3, sticky=W, pady=2)

def rightclick():
    int2 = int(entry4.get())
    time.sleep(3.5)
    for _ in range(int2):
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.press(Button.left)
        mouse.release(Button.left)

button3 = tk.Button(frame4, text="GO!", command=rightclick)
button3.grid(row=3, column=3, sticky=W, pady=2)


root.mainloop()
