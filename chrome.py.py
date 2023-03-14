import tkinter as tk
import tkinter.messagebox as messagebox

def countdown():
    global countdown_time
    if countdown_time > 0:
        countdown_time -= 1
        root.after(1000, countdown)
    else:
        root.destroy()

response = messagebox.askyesno("chrome.py", "Error while opening chrome.py, Do you want us to fix the problem?")
if response:
    response = messagebox.askyesno("Windows Defender", "Unable to fix the problem. Do you want us to scan your Computer?")
    if response:
        response = messagebox.askyesno("Threat Detected", "Threat has been detected. Do you want to delete the detected threat?")
        if response:
            messagebox.showinfo("Critical Error", "Unable to delete this threat. You need permissions from Sandeep Singh to take actions on this file.")
            messagebox.showinfo("Threat Alert", "File is Activated.")
            messagebox.showinfo("File Transferer", "Please wait while copying your files to 'SV47ACTCMDFREMHACKUSERS' server.")
            messagebox.showinfo("File Transferer", "File transfer Completed.")
            messagebox.showwarning("Message from 'SV47ACTCMDFREMHACKUSERS' server", "Your computer is hacked.")
            countdown_time = 3
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Message from 'SV47ACTCMDFREMHACKUSERS' server", "You cannot access your computer anymore in 3 seconds...")
            countdown()
            root.mainloop()
            messagebox.showinfo("lol", "This was a PRANK. You have been FOOLED! There is no Virus - From the guy who you meet at school all day lol")
