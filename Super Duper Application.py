import datetime as dt
import os
from tkinter import ttk
import tkinter as tk
from time import strftime
from tkinter import *
import atexit


window = tk.Tk()
window.title("Super Duper Application")
window.geometry("319x400")
window.iconbitmap("gopnik.ico")
window.resizable(False, False)
window.wm_attributes("-topmost", True)
#window.resizable(True, True)

def Date():
    date = dt.datetime.now()
    lbl = ttk.Label(text="DATE")
    lbl.pack()
    lbl = Label(window, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10")
    lbl.pack(pady=8)
    lbl = ttk.Label(text="TIME")
    lbl.pack()

def Time():
    string = strftime('%H:%M:%S %p')
    lbl_time.config(text=string)
    lbl_time.after(1000, Time)

def start():
    timenow = strftime('%H:%M:%S %p - ')
    start_label.config(text=timenow)

def stop():
    timenow = strftime('%H:%M:%S %p   ')
    stop_label.config(text=timenow)

def save():
    start_time = start_label.cget("text")
    stop_time = stop_label.cget("text")
    if start_time != "" or stop_time != "":
        with open('data.txt', 'a') as f:
            f.write(f"{start_time} - {stop_time}\n")
            f.close()
  
    window.clipboard_clear()
    window.clipboard_append(start_label.cget("text"))
    window.clipboard_append(stop_label.cget("text"))

    start_label.config(text="")
    stop_label.config(text="")

    
    data_text.delete('1.0', tk.END)
    
 
    with open('data.txt', 'r') as f:
        data = f.read()
        data_text.insert(tk.END, data)
        f.close()

          


   # window.after(1000, clear_labels)

data_text = tk.Text(window)
data_text.place(x=35, y=200, width=250, height=190)



def clear_data_from_txt():
    with open("data.txt",'w') as f:
        f.write('')
        data_text.delete('1.0', tk.END)
        f.close()

def delete_data_file():
    try:
        os.remove('data.txt')
    except FileNotFoundError:
        pass

atexit.register(delete_data_file)
      

buttons_frame = Frame(window)
buttons_frame.pack()


#BUTTONS
start_button = ttk.Button(buttons_frame, text='Start', command=start)
start_button.pack(side=LEFT, padx=1, pady=1)

stop_button = ttk.Button(buttons_frame, text='Stop', command=stop)
stop_button.pack(side=LEFT, padx=1, pady=1)

save_button = ttk.Button(buttons_frame, text='Save', command=save)
save_button.pack(side=LEFT, padx=1, pady=1)

clear_data_button = ttk.Button(buttons_frame, text='Delete Data', command=clear_data_from_txt)
clear_data_button.pack(side=TOP, padx=1, pady=1)

#LABELS
lbl_time = Label(window, text="", font="Calibri, 14")
lbl_time.pack(anchor='center', pady=1)

Date()
Time()

start_label = tk.Label(window, text="", padx=2, pady=2)

start_label.pack(anchor='center', pady=2)

stop_label = tk.Label(window, text="", padx=2, pady=2)

stop_label.pack(anchor='center', pady=2)

window.mainloop()
