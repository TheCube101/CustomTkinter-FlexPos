from customtkinter import *

class FlexGrid:
    def __init__(self, root):
        self.root = root
        self.widgets = []
        self.default_widget_height = 40  # Default height for widgets

    def add_widget(self, widget, row, column, padx, pady, flex_size):
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky="ew")
        self.widgets.append({
            "widget": widget,
            "flex_size": flex_size,
            "padx": padx,
            "pady": pady
        })
        # Set column and row weights for resizing behavior
        self.root.grid_columnconfigure(column, weight=flex_size)
        self.root.grid_rowconfigure(row, weight=flex_size)

    def update_size(self, minimum_width, minimum_height, scaling_threshold):
        total_flex = sum(w["flex_size"] for w in self.widgets) or 1  # Avoid division by zero
        total_widgets = len(self.widgets)
        padx_total = sum(w["padx"] for w in self.widgets) * (total_widgets + 1)
        pady_total = sum(w["pady"] for w in self.widgets) * (total_widgets + 1)

        # Calculate available width and height, subtracting total padding
        available_width = self.root.winfo_width() - padx_total
        available_height = self.root.winfo_height() - pady_total

        # Calculate width per widget, ensuring minimum width
        width = max((available_width // total_flex), minimum_width)

        # Decide height: Use default unless the width is below the scaling threshold
        if width < scaling_threshold:
            # If width is too small, increase height proportionally
            height = max((available_height // total_widgets), minimum_height)
        else:
            # Otherwise, use the default height
            height = self.default_widget_height

        # Update each widget's dimensions
        for entry in self.widgets:
            widget = entry["widget"]
            widget.configure(width=width, height=height)

# Set up root window
root = CTk()
root.geometry("960x540")
root.iconbitmap("")  # Remember file must be .ico
root.title("")
set_appearance_mode("system")
deactivate_automatic_dpi_awareness()
set_widget_scaling(2)
set_window_scaling(2)

# Create FlexGrid instance
flex_grid = FlexGrid(root)

# Create buttons and add them with flex sizes
button1 = CTkButton(master=root, text="Button 1", corner_radius=20)
button2 = CTkButton(master=root, text="Button 2", corner_radius=20)
button3 = CTkButton(master=root, text="Button 3", corner_radius=20)
button4 = CTkButton(master=root, text="Button 4", corner_radius=20)

# Register buttons with flex properties in the FlexGrid
flex_grid.add_widget(button1, row=0, column=0, padx=20, pady=20, flex_size=1)
flex_grid.add_widget(button2, row=0, column=1, padx=20, pady=20, flex_size=1)
flex_grid.add_widget(button3, row=0, column=2, padx=20, pady=20, flex_size=1)
flex_grid.add_widget(button4, row=0, column=3, padx=20, pady=20, flex_size=1)

# Bind resize event to update sizes based on flex properties
# The scaling_threshold determines when to scale height
root.bind("<Configure>", lambda event: flex_grid.update_size(minimum_width=500, minimum_height=50, scaling_threshold=500))

root.mainloop()