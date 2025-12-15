#!/usr/bin/python3
# Change the above line to point to "/usr/bin/python" installation if necessary
# Description: This file is used to create a GUI for the EMG project. The GUI will be used to monitor the power consumption of the vitals.

from guizero import App, Slider, Text
from gpiozero import Motor
from CurvedBar import CurvedBar



app = App("Monitior")
app.tk.attributes("-fullscreen", True)

height = app.tk.winfo_screenheight()
width = app.tk.winfo_screenwidth()

print(height)
print(width)

# Add the curved bar
curved_bar = CurvedBar(app, width=width/3, height=height/2, max_value=100, benchmark={"amber": 50, "red": 75}, title="Power Consumption")

actual_value = 0
motor_power = 10

# Main application
def update_bar(value):
    curved_bar.check_benchmark()
    curved_bar.set_value(int(value))

def on_value_change(var, value):
    var.set(value)

# Add a slider to control the curved bar
Text(app, text="Adjust adjust actual value Value:")
slider = Slider(app, start=0, end=100, width=300, command=update_bar)
# Text(app, text="Adjust Motor Value:")
# slider = Slider(app, start=0, end=100, width=300, command=update_bar)

app.display()