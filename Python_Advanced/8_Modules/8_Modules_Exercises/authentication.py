import json
from tkinter import *

from canvas import tk
from helpers import clean_screen
from products import render_products

def login(username, pword):
    with open("db/user_credentials_db.txt", "r") as file:
        data = file.readlines()
        for line in data:
            name, password = line[:-1].split(", ")
            if name == username and pword == password:
                render_products()
                return

        render_login(error="Invalid username or password")

def render_login(error=None):
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)

    if error is not None:
        Label(tk, text="Invalid username or password").grid(row=3, column=0)
    Button(tk, text="Enter", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2, column=0)


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg="white",command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black").grid(row=0, column=1, sticky="e")

