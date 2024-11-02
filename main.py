from customtkinter import *


class FlexGrid:
    def __init__(self, root):
        self.root = root
        self.widgets = []
        self.default_widget_height = 40  # Default height for widgets
        self.resize_id = None

    def add_widget(self, widget, row, column, padx, pady, flex_size):
        # Store widget with its grid info
        self.widgets.append({
            "widget": widget,
            "row": row,
            "column": column,
            "padx": padx,
            "pady": pady,
            "flex_size": flex_size
        })
        # Set initial grid placement
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky="ew")
        # Configure the grid weights for resizing behavior
        self.root.grid_columnconfigure(column, weight=flex_size)
        self.root.grid_rowconfigure(row, weight=flex_size)

    def update_size(self, minimum_width, minimum_height, scaling_threshold, width_buffer):
        total_flex = sum(w["flex_size"] for w in self.widgets) or 1  # Avoid division by zero
        padx_total = sum(w["padx"] for w in self.widgets)
        pady_total = sum(w["pady"] for w in self.widgets)
        widget_padx = self.widgets[0]["widget"].grid_info()["padx"]
        widget_pady = self.widgets[0]["widget"].grid_info()["pady"]
        # Calculate available width and height
        available_width = self.root.winfo_width() - padx_total
        width_per_flex_unit = available_width // total_flex

        # Calculate width per widget, ensuring minimum width
        width = max(width_per_flex_unit, minimum_width)
        
        rows_with_widgets = set()
        
        for entry in self.widgets:
            widget = entry["widget"]
            row = widget.grid_info()["row"]
            rows_with_widgets.add(row)

        rows_widgets_count = len(rows_with_widgets)

        available_height = rows_widgets_count / widget_pady + self.default_widget_height
        print(f"Available height: {available_height}")
        # available_height = (total amount of rows)/paddingY*2 + widgets height

        # Decide height based on scaling
        if width <= scaling_threshold:
            height = 200

        else:
            height = self.default_widget_height

        # Adjust widget positions and update their sizes
        current_row = 0
        current_column = 0

        for entry in self.widgets:
            widget = entry["widget"]
            padx = entry["padx"]
            pady = entry["pady"]

            # Check if the widget needs to move to the next row
            if (current_column + 1) * (width + padx) > available_width:
                current_row += 1
                current_column = 0

            # Update the widget's grid position
            widget.grid(row=current_row, column=current_column, padx=padx, pady=pady, sticky="ew")
            widget.configure(width=width, height=height)

            current_column += 1

    def on_resize(self, event, minimum_width, minimum_height, scaling_threshold, width_buffer):
        if self.resize_id is not None:
            self.root.after_cancel(self.resize_id)
        self.resize_id = self.root.after(200, self.update_size, minimum_width, minimum_height, scaling_threshold, width_buffer)


    def on_resize(self, event, minimum_width, minimum_height, scaling_threshold, width_buffer):
        if self.resize_id is not None:
            self.root.after_cancel(self.resize_id)
        self.resize_id = self.root.after(200, self.update_size, minimum_width, minimum_height, scaling_threshold, width_buffer)

# Set up root window
root = CTk()
root.geometry("1000x540")
root.title("CustomTkinter-FlexPos")
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
flex_grid.add_widget(button1, row=0, column=0, padx=20, pady=20, flex_size=2)
flex_grid.add_widget(button2, row=0, column=1, padx=20, pady=20, flex_size=2)
flex_grid.add_widget(button3, row=0, column=2, padx=20, pady=20, flex_size=2)
flex_grid.add_widget(button4, row=0, column=3, padx=20, pady=20, flex_size=2)

# Bind resize event to update sizes based on flex properties
# The scaling_threshold determines when to scale height
root.bind("<Configure>", lambda event: flex_grid.on_resize(event, minimum_width=300, minimum_height=50, scaling_threshold=300, width_buffer=200))

root.mainloop()