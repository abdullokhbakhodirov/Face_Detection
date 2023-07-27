# This window blocker creates black window which can't be closed. 
# It will be closed only that time when it detects trained face 

import tkinter as tk
import keyboard
import threading
from face_recognitions3 import recognizer

def create_black_window():
    def on_escape(event):
        window.destroy()

    def check_wrapper():
        result = recognizer()
        if result:
            window.destroy()
        else:
            check_wrapper()
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.configure(bg="black")
    window.overrideredirect(True)
    keyboard.add_hotkey("alt + tab", lambda: None, suppress=True)
    keyboard.add_hotkey("win", lambda: None, suppress=True)
    check_thread = threading.Thread(target=check_wrapper)
    check_thread.daemon = True
    check_thread.start()
    window.mainloop()

create_black_window()
