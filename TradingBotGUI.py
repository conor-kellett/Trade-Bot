import tkinter as tk
from tkinter import ttk, message 

class TradeBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Trade Bot")
        self.equities = self.load_equities()
