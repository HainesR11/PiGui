from logger import logger
import tkinter as tk
import math

class CurvedBar:

    def __init__(self, parent, width=300, height=300, max_value=100, benchmark={'amber': 50, 'red': 80}):
        self.benchmark_color = '#00ff00'
        self.max_value = max_value
        self.current_value = 0
        self.benchmark = benchmark
        self.start_angle = 180
        self.extent = 0
        self.center = (width // 2, height // 2)

        self.radius = min(width, height) // 2 - 20

        # Create a Canvas widget
        self.canvas = tk.Canvas(parent.tk, width=width, height=height)
        self.canvas.pack()

        self.width = width
        self.height = height

        # Draw static background arc
        self.canvas.create_arc(20, 20, width-20, height-20, start=0, extent=180, outline='#ddd', width=15, style=tk.ARC)

        # Foreground arc for progress
        self.progress_arc = self.canvas.create_arc(20, 20, width-20, height-20, start=180, extent=0,
                                                   outline=self.benchmark_color, width=15, style=tk.ARC)

        # Text to show percentage
        self.value_label = self.canvas.create_text(width // 2, height // 2, text="0% power", font=("Arial", 20), fill="white")

    def check_benchmark(self):
        if self.current_value >= self.benchmark["red"]:
            self.canvas.itemconfig(self.progress_arc, outline='#ff0000')
        elif self.current_value >= self.benchmark["amber"]:
            self.canvas.itemconfig(self.progress_arc, outline='#ffcc00')
        else:
            self.canvas.itemconfig(self.progress_arc, outline='#00ff00')

    def set_value(self, value):
        """Update the curved bar progress and percentage label."""
        self.current_value = min(max(value, 0), self.max_value)  # Clamp the value
        extent = -(self.current_value / self.max_value) * 180   # Map value to arc extent
        self.extent = extent
        self.canvas.itemconfig(self.progress_arc, extent=extent)
        self.canvas.itemconfig(self.value_label, text=f"{int((self.current_value / self.max_value) * 100)}% Power")