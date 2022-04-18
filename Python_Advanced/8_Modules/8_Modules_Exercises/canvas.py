
from tkinter import *  # first import library for windows

def create_app():
    tk=Tk()
    tk.geometry("700x600+0+0")
    tk.title("GUI product shop")
    return tk

tk=create_app()




#
# import tkinter as tk
#
# """ HERE IS ALL, how looks the window, have to put in a function"""
# window=tk.Tk()
# window.geometry("700x600+0+0") # size
# window.title("GUI product shop") # name up
# greeting = tk.Label(text="Hello, DENISLAV") # labels
# label = tk.Label(
#     text="SHALL WE START?",
#     foreground="white",  # Set the text color to white
#     background="blue"  # Set the background color to black
# )
# label.place(x=0,y=0)
# button = tk.Button(
#     window,
#     text="Click me!",
#     width=10,
#     height=10,
#     bg="blue",
#     fg="yellow",
#     command="Hello"
# ).grid(row=4,column=0)
#
# entry = tk.Entry(fg="black", bg="white", width=50)
#
# #text_box = tk.Text()
# #text_box.pack()
# label1 = tk.Label(master=window, text="Login", bg="green")
# label1.place(x=0, y=0)
# label2 = tk.Label(master=window, text="Register", bg="yellow")
# label2.place(x=40, y=0)
#
# entry.pack()
# button.pack(pady=20)
# greeting.pack()
# label.pack()
#
#
# name=entry.get()
# print(name)
#
# tk.mainloop()