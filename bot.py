import tkinter as tk
from tkinter import ttk, message 
import json
import time
import threading
import random

DATA_FILE = "equities.json"

def fetch_mock_api(symbol):
    return {
        "price": 100
    }

def mock_chatgpt_response(message):
    return f"Mock response to: {message}"

