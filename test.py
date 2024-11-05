from customtkinter import *


class FlexGrid:
    def __init__(self, root):
        self.root = root
        self.widgets = []
        self.default_widget_height = 0  # Default height for widgets
        self.resize_id = None
        self.current_row = 0
        self.current_column = 0

    def add_widget(self, widget, padx, pady):
        flex_size = 2
        # Store widget with its grid info
        self.widgets.append({
            "widget": widget,
            "row": self.current_row,
            "column": self.current_column,
            "padx": padx,
            "pady": pady,
            "flex_size": flex_size
        })
        # Set initial grid placement
        widget.grid(row=self.current_row, column=self.current_column, padx=padx, pady=pady, sticky="e")

        # Configure the grid weights for resizing behavior
        self.root.grid_columnconfigure(self.current_column, weight=flex_size)
        self.root.grid_rowconfigure(self.current_row, weight=flex_size)

        # Move to the next column
        self.current_column += 1
        self.current_row += 1

    def update_size(self, minimum_width, minimum_height, flex, flex_max):
        total_flex = sum(w["flex_size"] for w in self.widgets) or 1  # Avoid division by zero
        padx_total = sum(w["padx"] for w in self.widgets)
        pady_total = sum(w["pady"] for w in self.widgets)

        rows_with_widgets = set()
        for entry in self.widgets:
            widget = entry["widget"]
            row = widget.grid_info()["row"]
            rows_with_widgets.add(row)

        rows_widgets_count = len(rows_with_widgets)

        # Calculate available width and height
        available_width = self.root.winfo_width() - padx_total
        available_height = self.root.winfo_height() - pady_total

        width_per_flex_unit = available_width // total_flex
        height_per_flex_unit = available_height // rows_widgets_count

        # Calculate width/height per widget, ensuring minimum width/height
        width = max(width_per_flex_unit, minimum_width)
        height = max(height_per_flex_unit, minimum_height)

        # Adjust widget positions and update their sizes
        current_row = 0
        current_column = 0
            
        for entry in self.widgets:
            widget = entry["widget"]
            padx = entry["padx"]
            pady = entry["pady"]

            if flex == True != False:
                if (current_column + 1) * (width + padx) > available_width:
                    current_row += 1
                    current_column = 0

                
            elif flex_max > 0 != None:
                if current_column >= flex_max or (current_column + 1) * (width + padx) > available_width:
                    current_row += 1
                    current_column = 0
                    

            # Update the widget's grid position
            widget.grid(row=current_row, column=current_column, padx=padx, pady=pady, sticky="e")
            widget.configure(width=width, height=height)

            current_column += 1

    def on_resize(self, event, minimum_width, minimum_height, flex, flex_max=None):
        if self.resize_id is not None:
            self.root.after_cancel(self.resize_id)
        self.resize_id = self.root.after(100, self.update_size, minimum_width, minimum_height, flex, flex_max)


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
button5 = CTkButton(master=root, text="Button 5", corner_radius=20)
button6 = CTkButton(master=root, text="Button 6", corner_radius=20)
button7 = CTkButton(master=root, text="Button 7", corner_radius=20)

# Register buttons with flex properties in the FlexGrid
flex_grid.add_widget(button1, padx=20, pady=20)
flex_grid.add_widget(button2, padx=20, pady=20)
flex_grid.add_widget(button3, padx=20, pady=20)
flex_grid.add_widget(button4, padx=20, pady=20)
flex_grid.add_widget(button5, padx=20, pady=20)
flex_grid.add_widget(button6, padx=20, pady=20)
flex_grid.add_widget(button7, padx=20, pady=20)

# Bind resize event to update sizes based on flex properties
root.bind("<Configure>", lambda event: flex_grid.on_resize(event, minimum_width=300, minimum_height=150, flex=True, flex_max=None))

root.mainloop()