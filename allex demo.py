import tkinter as tk
from datetime import datetime

def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=f"Current time: {current_time}")

root = tk.Tk()
root.title("Clock")
root.geometry("300x150")

label = tk.Label(root, text="Click the button to get the time", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Get Current Time", command=show_time, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
