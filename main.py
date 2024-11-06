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


    def update_size(self, minimum_width, minimum_height, flex_max, flex=False, flex_wrap="wrap", flex_growX=1, flex_growY=1):
        # Ensure flex_max is an integer
        flex_max = int(flex_max) if flex_max is not None else 0
        
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
        width = max(width_per_flex_unit, minimum_width) * flex_growX
        height = max(height_per_flex_unit, minimum_height) * flex_growY

        # Adjust widget positions and update their sizes
        current_row = 0
        current_column = 0
            
        for entry in self.widgets:
            widget = entry["widget"]
            padx = entry["padx"]
            pady = entry["pady"]

            if flex == False != True:
                if (current_column + 1) * (width + padx) > available_width:
                    current_row += 1
                    current_column = 0

            elif flex_max is not None and flex_max > 0:
                if current_column >= flex_max or (current_column + 1) * (width + padx) > available_width:
                    current_row += 1
                    current_column = 0

            elif flex_wrap:
                if flex_wrap == "wrap":
                    if (current_column + 1) * (width + padx) > available_width:
                        current_row += 1
                        current_column = 0
                elif flex_wrap == "nowrap":
                    if (current_column + 1) > available_width:
                        current_column += 1
                else:
                    print("returned")
                    return

            # Update the widget's grid position
            widget.grid(row=current_row, column=current_column, padx=padx, pady=pady, sticky="e")
            widget.configure(width=width, height=height)

            current_column += 1


    def on_resize(self, event, minimum_width, minimum_height, flex=False, flex_max=None, flex_wrap="wrap", flex_growX=1, flex_growY=1):
        if self.resize_id is not None:
            self.root.after_cancel(self.resize_id)
        self.resize_id = self.root.after(100, self.update_size, minimum_width, minimum_height, flex, flex_max, flex_wrap, flex_growX, flex_growY)


    def flex_setup(self, minimum_width, minimum_height, flex=False, flex_max=None, flex_wrap=None, flex_growX=1, flex_growY=1):
        self.root.bind("<Configure>", lambda event: self.on_resize(event, minimum_width, minimum_height, flex, flex_max, flex_wrap, flex_growX, flex_growY))