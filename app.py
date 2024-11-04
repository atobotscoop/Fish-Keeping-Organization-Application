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

# Utility function to clear entry fields
def clear_entries():
    for entry in [entry_fish_name, entry_category_name, entry_tank_name, entry_compatibility, entry_temp_range, entry_food_name,
                  entry_new_food_name, entry_new_food_type, entry_new_food_perishable, entry_new_tank_size, entry_new_tank_type, entry_new_tank_currentfish,
                  entry_fish_search, entry_food_search, entry_tank_search]:
        entry.delete(0, tk.END)

# Functions to search by name and display results
def search_fish():
    fish_listbox.delete(0, tk.END)
    fish_name = entry_fish_search.get()
    cursor.execute('''SELECT Fish.Name, Category.Type, Tank.Size, Fish.Compatibility, Fish.TemperatureRange, Food.Name
                      FROM Fish
                      LEFT JOIN Food ON Fish.FoodID = Food.FoodID
                      LEFT JOIN Tank ON Fish.TankID = Tank.TankID
                      LEFT JOIN Category ON Fish.CategoryID = Category.CategoryID
                      WHERE Fish.Name LIKE ?''', (f"%{fish_name}%",))
    for fish in cursor.fetchall():
        fish_listbox.insert(tk.END, f"Name: {fish[0]}, Category: {fish[1]}, Tank: {fish[2]}, "
                                    f"Compatibility: {fish[3]}, Temp Range: {fish[4]}, Food: {fish[5]}")
#Search food function
def search_food():
    food_listbox.delete(0, tk.END)
    food_name = entry_food_search.get()
    cursor.execute("SELECT Name, FoodType, Perishable FROM Food WHERE Name LIKE ?", (f"%{food_name}%",))
    for food in cursor.fetchall():
        food_listbox.insert(tk.END, f"Name: {food[0]}, Type: {food[1]}, Perishable: {food[2]}")
# Search tank function
def search_tank():
    tank_listbox.delete(0, tk.END)
    tank_size = entry_tank_search.get()
    cursor.execute("SELECT Size, Type, CurrentFish FROM Tank WHERE Size LIKE ?", (f"%{tank_size}%",))
    for tank in cursor.fetchall():
        tank_listbox.insert(tk.END, f"Size: {tank[0]}, Type: {tank[1]}, Current Fish: {tank[2]}")

# CRUD functions for adding Fish, Food, and Tank
def add_fish():
    name = entry_fish_name.get()
    category_name = entry_category_name.get()
    tank_name = entry_tank_name.get()
    compatibility = entry_compatibility.get()
    temp_range = entry_temp_range.get()
    food_name = entry_food_name.get()

    cursor.execute('''SELECT CategoryID FROM Category WHERE Type = ?''', (category_name,))
    category_id = cursor.fetchone()
    cursor.execute('''SELECT TankID FROM Tank WHERE Size = ?''', (tank_name,))
    tank_id = cursor.fetchone()
    cursor.execute('''SELECT FoodID FROM Food WHERE Name = ?''', (food_name,))
    food_id = cursor.fetchone()

    if category_id and tank_id and food_id:
        cursor.execute("INSERT INTO Fish (Name, CategoryID, TankID, Compatibility, TemperatureRange, FoodID) VALUES (?, ?, ?, ?, ?, ?)", 
                       (name, category_id[0], tank_id[0], compatibility, temp_range, food_id[0]))
        connection.commit()
        messagebox.showinfo("Success", "Fish added successfully.")
        clear_entries()
        search_fish()  # Refresh the fish search results after adding
    else:
        messagebox.showerror("Error", "Invalid Category, Tank, or Food name.")



#scrollable feature and search bars for each table
# Fish Search 
fish_frame = tk.LabelFrame(main_frame, text="Fish Information", padx=10, pady=10)
fish_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

tk.Label(fish_frame, text="Search Fish by Name").pack()
entry_fish_search = tk.Entry(fish_frame)
entry_fish_search.pack()
tk.Button(fish_frame, text="Search Fish", command=search_fish).pack(pady=2)

scrollbar_fish = tk.Scrollbar(fish_frame)
fish_listbox = tk.Listbox(fish_frame, yscrollcommand=scrollbar_fish.set, width=60, height=10)
scrollbar_fish.config(command=fish_listbox.yview)
scrollbar_fish.pack(side=tk.RIGHT, fill=tk.Y)
fish_listbox.pack(padx=10, pady=10)

# We can now search for food
food_frame = tk.LabelFrame(main_frame, text="Food Information", padx=10, pady=10)
food_frame.grid(row=0, column=1, padx=10, pady=10, sticky='ns')

tk.Label(food_frame, text="Search Food by Name").pack()
entry_food_search = tk.Entry(food_frame)
entry_food_search.pack()
tk.Button(food_frame, text="Search Food", command=search_food).pack(pady=2)

scrollbar_food = tk.Scrollbar(food_frame)
food_listbox = tk.Listbox(food_frame, yscrollcommand=scrollbar_food.set, width=60, height=10)
scrollbar_food.config(command=food_listbox.yview)
scrollbar_food.pack(side=tk.RIGHT, fill=tk.Y)
food_listbox.pack(padx=10, pady=10)

#We can also now search for tanks
tank_frame = tk.LabelFrame(main_frame, text="Tank Information", padx=10, pady=10)
tank_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ns')

tk.Label(tank_frame, text="Search Tank by Size").pack()
entry_tank_search = tk.Entry(tank_frame)
entry_tank_search.pack()
tk.Button(tank_frame, text="Search Tank", command=search_tank).pack(pady=2)

scrollbar_tank = tk.Scrollbar(tank_frame)
tank_listbox = tk.Listbox(tank_frame, yscrollcommand=scrollbar_tank.set, width=60, height=10)
scrollbar_tank.config(command=tank_listbox.yview)
scrollbar_tank.pack(side=tk.RIGHT, fill=tk.Y)
tank_listbox.pack(padx=10, pady=10)

tk.Label(fish_frame, text="Fish Name").pack()
entry_fish_name = tk.Entry(fish_frame)
entry_fish_name.pack()

tk.Label(fish_frame, text="Category").pack()
entry_category_name = tk.Entry(fish_frame)
entry_category_name.pack()

tk.Label(fish_frame, text="Tank Size").pack()
entry_tank_name = tk.Entry(fish_frame)
entry_tank_name.pack()

tk.Label(fish_frame, text="Compatibility").pack()
entry_compatibility = tk.Entry(fish_frame)
entry_compatibility.pack()

tk.Label(fish_frame, text="Temperature Range").pack()
entry_temp_range = tk.Entry(fish_frame)
entry_temp_range.pack()

tk.Label(fish_frame, text="Food").pack()
entry_food_name = tk.Entry(fish_frame)
entry_food_name.pack()

# Add Fish Button
tk.Button(fish_frame, text="Add Fish", command=add_fish).pack(pady=2)



# Allow scrolling of the area
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all")) #Basically the scroll region(Kind of like unity scroll rect)

main_frame.bind("<Configure>", on_configure) #basically allows

root.mainloop()

#close the connection
connection.close()
