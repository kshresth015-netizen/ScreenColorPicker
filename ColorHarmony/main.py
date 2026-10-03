from color_engine import (
    hex_to_rgb,
    rgb_to_hex,
    rgb_to_hsv,
    hsv_to_rgb,
    get_complementary,
    get_analogous,
    get_triadic,
    get_tetradic
)
# from color_engine import (
#     get_complementary,
#     get_analogous,
#     get_triadic,
#     get_tetradic,
#     get_split_complementary,
#     get_monochromatic
# )

import tkinter as tk

root = tk.Tk()
root.title("Color Harmony")
root.geometry("800x600")
title = tk.Label(
    root,
    text="Color Harmony Tool",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)

root.mainloop()

def create_color_swatch(parent, color):
    frame = tk.Frame(parent)

    preview = tk.Frame(
        frame,
        width=100,
        height=60,
        bg=color
    )

    preview.pack()

    label = tk.Label(
        frame,
        text=color
    )

    label.pack()

    return frame
