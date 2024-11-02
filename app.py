import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database connection to MySQLite
connection = sqlite3.connect('DataBasesProject1.db')
cursor = connection.cursor()

#Main window
root = tk.Tk()
root.title("Fishkeeping Database Management") #Window title
root.geometry("900x700") #size of window

# Create a Canvas and a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)#scrollbar to control vertical scrolling(y axis)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)# Put scrollbar to the right side of the window

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #Fill the window
canvas.configure(yscrollcommand=scrollbar.set)# Sets the scroll bar

#Content holder
main_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=main_frame, anchor='nw') #Creates a winow in tgge canvas for our stuff



# Allow scrolling of the area
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all")) #Basically the scroll region(Kind of like unity scroll rect)

main_frame.bind("<Configure>", on_configure) #basically allows the above event to be invoked

root.mainloop()

#close the connection
connection.close()
