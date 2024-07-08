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


def create_bar_graph(pizzas, quantities_sold):
    # Create bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(pizzas, quantities_sold)
    ax.set_title("Number of Each Type of Pizza Sold")
    ax.set_xlabel("Pizza")
    ax.set_ylabel("Quantity Sold")
    ax.set_xticks(range(len(pizzas)))
    ax.set_xticklabels(pizzas, rotation=45, ha="right")

    # Adding extra info for the client
    total_sold = sum(quantities_sold)
    ax.text(
        0.5,
        0.95,
        f"Total Pizzas Sold: {total_sold}",
        transform=ax.transAxes,
        ha="center",
    )
    
    average_sold = total_sold / len(pizzas)
    ax.text(
        0.5, 
        0.90,
        f"Average Pizzas Sold: {average_sold:.2f}",
        transform=ax.transAxes,
        ha="center",
    )
    
    best_seller = pizzas[quantities_sold.index(max(quantities_sold))]
    ax.text(
        0.5, 0.85, f"Best Seller: {best_seller}", transform=ax.transAxes, ha="center"
    )
    worst_seller = pizzas[quantities_sold.index(min(quantities_sold))]
    ax.text(
        0.5, 0.80, f"Worst Seller: {worst_seller}", transform=ax.transAxes, ha="center"
    )

    return fig


def display_chart_in_tkinter_window(fig):
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


if __name__ == "__main__":
    # Sample data 
    pizzas = [
        "Precious Pepperoni",
        "Supreme Chicken of Gondor",
        "Bag-End BBQ Meatlovers",
        "Fellowship of the Four Cheeses",
        "Bree Ham & Pineapple",
        "Leaf of Lorien Margherita",
    ]
    
    quantities_sold = [1, 5, 2, 0, 0, 3]

    fig = create_bar_graph(pizzas, quantities_sold)
    display_chart_in_tkinter_window(fig)
