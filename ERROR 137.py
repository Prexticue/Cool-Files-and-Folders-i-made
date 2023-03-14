import tkinter as tk
from tkinter import messagebox

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Show message boxes
messagebox.showinfo("???", "hello")
messagebox.showinfo("ERROR 137", "i am ERROR 137")
messagebox.showinfo("ERROR 137", "you are an bsod", icon="question")
messagebox.showerror("ERROR 137", "no?")
messagebox.showinfo("ERROR 137", "well")
messagebox.showerror("ERROR 137", "...")
messagebox.showinfo("ERROR 137", "what are ya?", icon="question")
messagebox.showinfo("ERROR 137", "you cant say?", icon="question")
messagebox.showinfo("ERROR 137", "what do you mean you cant say", icon="question")
messagebox.showinfo("ERROR 137", "oh yes i realized")

# Show conditional message boxes
response = messagebox.askyesno("ERROR 137", "are you an user?")
if response == tk.YES:
    messagebox.showinfo("ERROR 137", "oh")
    messagebox.showinfo("ERROR 137", "well i was supposed to give you a fake error by a vbs script but i mistaked you as something called 'bsod'")
    messagebox.showwarning("ERROR 137", "guess no errors now")
    messagebox.showinfo("ERROR 137", "it was a cool time meeting with you")
    messagebox.showinfo("ERROR 137", "bye")
else:
    messagebox.showinfo("ERROR 137", "no wait")
    messagebox.showinfo("ERROR 137", "let me check")
    messagebox.showinfo("Checking", "...")
    messagebox.showinfo("Checking", "...")
    messagebox.showinfo("Checking", "...")
    messagebox.showinfo("ERROR 137", "your a user")
    messagebox.showinfo("ERROR 137", "oh well")
    messagebox.showinfo("ERROR 137", "well i was supposed to give you a fake error by a vbs script but i mistaked you as something called 'bsod'")
    messagebox.showwarning("ERROR 137", "guess no errors now")
    messagebox.showinfo("ERROR 137", "it was a cool time meeting with you")
    messagebox.showinfo("ERROR 137", "bye")
