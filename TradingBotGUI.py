import tkinter as tk
from tkinter import ttk, message 

class TradingBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Trading Bot")
        self.create_widgets()
        self.load_data()
