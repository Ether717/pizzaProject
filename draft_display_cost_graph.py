"""
this is my idea for using tkinter with matplotlib to create a GUI with extra info for the client at a industry standard levels
ref link - https://www.youtube.com/watch?v=8exB6Ly3nx0
"""

import matplotlib

matplotlib.use("Agg")  # Use the Agg backend for Matplotlib
import matplotlib.pyplot as plt
from tkinter import Tk, Label
from PIL import Image, ImageTk
import io

# Sample data
pizzas = [
    "Precious Pepperoni",
    "Supreme Chicken of Gondor",
    "Bag-End BBQ Meatlovers",
    "Fellowship of the Four Cheeses",
    "Bree Ham & Pineapple",
    "Leaf of Lorien Margherita",
]
quantities_sold = [120, 85, 95, 110, 80, 75]


# Create bar chart using Matplotlib
fig, ax = plt.subplots()
ax.bar(pizzas, quantities_sold)
ax.set_title("Number of Each Type of Pizza Sold")
ax.set_xlabel("Pizza")
ax.set_ylabel("Quantity Sold")
ax.set_xticks(range(len(pizzas)))
ax.set_xticklabels(pizzas, rotation=45, ha="right")


# Save the plot to a BytesIO object
buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
plt.close(fig)  # Close the figure to free up memory

# Create the Tkinter window
root = Tk()
root.title("Pizza Sales Chart")

# Convert the BytesIO object to a PIL Image and then to an ImageTk object
image = Image.open(buf)
tk_image = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
label = Label(root, image=tk_image)
label.pack()

# Run the Tkinter event loop
root.mainloop()
