import tkinter as tk
from tkinter import messagebox

# Create a MessageBox with a button and an icon
response = messagebox.showinfo(title="right?", message="this is not a .vbs file.. right?", icon="question", 
                                type="yesno")

# Check the user's response
if response == "yes":
    messagebox.showinfo(title="yaey", message="les go!! this is my first time getting correct", icon="info")
else:
    response = messagebox.showinfo(title="nooooo", message="aww man i have never gotten anything correct in my life :(", icon="info")
