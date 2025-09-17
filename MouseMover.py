import pyautogui
import threading
import tkinter as tk
import time

class MouseMover:
    def __init__(self):
        self.running = True
        self.thread = threading.Thread(target=self.move_mouse_loop)
        self.thread.daemon = True
        self.thread.start()

    def move_mouse_loop(self):
        while True:
            if self.running:
                self.move_mouse()
                self.simulate_keypress()
            time.sleep(240)  # Every 4 minutes

    def move_mouse(self):
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y + 1)
        pyautogui.moveTo(x, y)

    def simulate_keypress(self):
        pyautogui.press('shift')

    def toggle(self):
        self.running = not self.running

    def is_running(self):
        return self.running

def start_gui():
    mover = MouseMover()

    root = tk.Tk()
    root.title("Mouse & Keyboard Mover")

    def toggle_state():
        mover.toggle()
        toggle_button.config(text="Stop" if mover.is_running() else "Resume")

    toggle_button = tk.Button(root, text="Stop", command=toggle_state)
    toggle_button.pack(pady=20, padx=20)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
