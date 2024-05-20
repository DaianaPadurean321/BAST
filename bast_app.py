import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import pystray
from PIL import Image, ImageDraw, ImageTk
from posture_detector import PostureDetector


class BASTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BAST - Back Straight Tracker")
        self.posture_detector = PostureDetector()

        self.break_interval = 50 * 60  # Default break interval in seconds (50 minutes)
        self.notification_message = "Please straighten your back!"
        self.break_notification_message = "Time for a break!"

        self.setup_ui()
        self.create_tray_icon()
        self.start_posture_check()
        self.start_sedentary_check()

    def setup_ui(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.notification_label = ttk.Label(self.main_frame, text="Stand straight!")
        self.notification_label.grid(row=0, column=0, sticky=tk.W)
        self.notification_text = tk.StringVar(value=self.notification_message)
        self.notification_entry = ttk.Entry(self.main_frame, width=50, textvariable=self.notification_text)
        self.notification_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.break_label = ttk.Label(self.main_frame, text="Break Interval (minutes):")
        self.break_label.grid(row=1, column=0, sticky=tk.W)
        self.break_interval_var = tk.IntVar(value=self.break_interval // 60)
        self.break_entry = ttk.Entry(self.main_frame, width=50, textvariable=self.break_interval_var)
        self.break_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.save_button = ttk.Button(self.main_frame, text="Save", command=self.save_settings)
        self.save_button.grid(row=2, column=0, columnspan=2)

        # Add the logo as an icon in the app window
        self.logo_img = ImageTk.PhotoImage(file="bast_icon.png")
        self.logo_label = tk.Label(self.main_frame, image=self.logo_img)
        self.logo_label.grid(row=3, column=0, columnspan=2, pady=10)

    def save_settings(self):
        self.notification_message = self.notification_text.get()
        self.break_interval = self.break_interval_var.get() * 60
        messagebox.showinfo("Settings Saved", "Your settings have been saved.")

    def start_posture_check(self):
        def check_posture():
            while True:
                posture = self.posture_detector.detect_posture()
                if posture == "Slouch detected":
                    self.show_posture_notification()
                time.sleep(5)  # Check posture every 5 seconds

        self.posture_check_thread = threading.Thread(target=check_posture)
        self.posture_check_thread.daemon = True
        self.posture_check_thread.start()

    def start_sedentary_check(self):
        def check_sedentary():
            while True:
                if self.posture_detector.time_since_last_movement() > self.break_interval:
                    self.show_break_notification()
                time.sleep(60)  # Check sedentary status every 60 seconds

        self.sedentary_check_thread = threading.Thread(target=check_sedentary)
        self.sedentary_check_thread.daemon = True
        self.sedentary_check_thread.start()

    def show_posture_notification(self):
        messagebox.showwarning("BAST - Back Straight Tracker", self.notification_message)

    def show_break_notification(self):
        messagebox.showwarning("BAST - Back Straight Tracker", self.break_notification_message)

    def create_image(self):
        # Use the provided logo image
        return Image.open("bast_icon.png")

    def create_tray_icon(self):
        image = self.create_image()
        menu = pystray.Menu(pystray.MenuItem('Show', self.show_app), pystray.MenuItem('Exit', self.on_closing))
        self.icon = pystray.Icon("BAST", image, "BAST - Back Straight Tracker", menu)
        self.icon.run_detached()

    def show_app(self):
        self.root.deiconify()

    def hide_app(self):
        self.root.withdraw()

    def on_closing(self):
        self.posture_detector.release()
        self.icon.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BASTApp(root)
    root.protocol("WM_DELETE_WINDOW", app.hide_app)
    root.mainloop()
