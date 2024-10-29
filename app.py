import sqlite3
import tkinter as tk
from tkinter import messagebox

def connect_db():
    connection = sqlite3.connect('DataBasesProject1.db')
    return connection

