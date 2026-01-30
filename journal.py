#Importing required packages
import tkinter as tk
from tkinter import ttk
import pandas as pd



def devPanel():
    root = Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="superb_dev_settings").grid(column=0, row=0)
    ttk.Button(frame, text="add word").grid(column=1, row=0)


print("Hey friend, welcome to this journal thingy~!")
feeling = input("How are you doing today? (input 1 for dev panel)")
feeling = feeling.lower()
devPanel()
