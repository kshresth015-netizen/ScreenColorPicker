
import tkinter as tk

from color_engine import (
    get_complementary,
    get_analogous,
    get_triadic,
    get_tetradic,
    get_split_complementary,
    get_monochromatic
)


class ColorHarmonyApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Harmony Tool")
        self.root.geometry("900x700")
        self.root.minsize(650, 450)
        self.root.configure(bg="#F5F5F5")

        self.selected_color = "#3498DB"

        self.create_scrollable_area()
        self.create_title()
        self.create_color_preview()
        self.generate_harmonies()
        self.display_harmonies()

    def create_scrollable_area(self):
        self.canvas = tk.Canvas(
            self.root,
            bg="#F5F5F5",
            highlightthickness=0
        )

        self.scrollbar = tk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="#F5F5F5"
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfigure(
                self.canvas_window,
                width=event.width
            )
        )

        self.canvas.bind_all(
            "<MouseWheel>",
            self.on_mousewheel
        )

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_app
        )

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(
            int(-event.delta / 120),
            "units"
        )

    def close_app(self):
        self.canvas.unbind_all("<MouseWheel>")
        self.root.destroy()

    def create_title(self):
        title = tk.Label(
            self.scrollable_frame,
            text="Color Harmony Tool",
            font=("Arial", 24, "bold"),
            bg="#F5F5F5",
            fg="#222222"
        )

        title.pack(pady=(25, 10))

        subtitle = tk.Label(
            self.scrollable_frame,
            text="Explore beautiful color combinations",
            font=("Arial", 11),
            bg="#F5F5F5",
            fg="#666666"
        )

        subtitle.pack(pady=(0, 20))

    def create_color_preview(self):
        preview_container = tk.Frame(
            self.scrollable_frame,
            bg="#FFFFFF",
            padx=20,
            pady=15
        )

        preview_container.pack(pady=10)

        self.color_preview = tk.Frame(
            preview_container,
            width=250,
            height=100,
            bg=self.selected_color
        )

        self.color_preview.pack()
        self.color_preview.pack_propagate(False)

        self.color_label = tk.Label(
            preview_container,
            text=self.selected_color,
            font=("Arial", 16, "bold"),
            bg="#FFFFFF",
            fg="#222222"
        )

        self.color_label.pack(pady=(12, 0))

    def generate_harmonies(self):
        self.harmonies = {
            "Complementary": get_complementary(
                self.selected_color
            ),
            "Analogous": get_analogous(
                self.selected_color
            ),
            "Triadic": get_triadic(
                self.selected_color
            ),
            "Tetradic": get_tetradic(
                self.selected_color
            ),
            "Split Complementary": get_split_complementary(
                self.selected_color
            ),
            "Monochromatic": get_monochromatic(
                self.selected_color
            )
        }

    def create_swatch(self, parent, color):
        frame = tk.Frame(
            parent,
            bg="#FFFFFF",
            padx=5,
            pady=5
        )

        preview = tk.Frame(
            frame,
            width=100,
            height=60,
            bg=color
        )

        preview.pack()
        preview.pack_propagate(False)

        label = tk.Label(
            frame,
            text=color,
            font=("Arial", 10),
            bg="#FFFFFF",
            fg="#333333"
        )

        label.pack(pady=(6, 2))

        return frame

    def create_palette_section(self, parent, name, colors):
        section = tk.Frame(
            parent,
            bg="#FFFFFF",
            padx=15,
            pady=12,
            bd=0
        )

        section.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        title = tk.Label(
            section,
            text=name,
            font=("Arial", 14, "bold"),
            bg="#FFFFFF",
            fg="#222222"
        )

        title.pack(pady=(0, 8))

        colors_frame = tk.Frame(
            section,
            bg="#FFFFFF"
        )

        colors_frame.pack()

        if isinstance(colors, str):
            colors = (colors,)

        for color in colors:
            swatch = self.create_swatch(
                colors_frame,
                color
            )

            swatch.pack(
                side="left",
                padx=5,
                pady=5
            )

    def display_harmonies(self):
        for name, colors in self.harmonies.items():
            self.create_palette_section(
                self.scrollable_frame,
                name,
                colors
            )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ColorHarmonyApp()
    app.run()
