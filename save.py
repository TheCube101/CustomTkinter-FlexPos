from customtkinter import *

root = CTk()
root.geometry("960x540")
root.iconbitmap("")  # Remember file must be .ico
root.title("")
set_appearance_mode("system")
deactivate_automatic_dpi_awareness()
set_widget_scaling(2)
set_window_scaling(2)


def update_size(minimum_width, minimum_height, padx_info, pady_info, exclude_widgets):
    widget_height = 40

    # Ignore widgets that are in the exclude_widgets list
    total_buttons = sum(
        1 for widget in root.children.values()
        if widget.grid_info().get('row') == 0 and widget not in exclude_widgets
    )

    available_width = root.winfo_width() - (padx_info * (total_buttons + 1))  # Subtract total padding
    available_height = root.winfo_height() - (pady_info * (total_buttons + 1))

    width = max((available_width // total_buttons), minimum_width)  # Ensure minimum width
    height = max((available_height // total_buttons), minimum_height)

    if width < minimum_width + 2:
        widget_height = height

    button1.configure(width=width, height=widget_height)
    button2.configure(width=width, height=widget_height)
    button3.configure(width=width, height=widget_height)
    button4.configure(width=width, height=widget_height)

    print("Number of buttons in row 0:", total_buttons)

# Create buttons

button1 = CTkButton(master=root, corner_radius=20)
button2 = CTkButton(master=root, corner_radius=20)
button3 = CTkButton(master=root, corner_radius=20)
button4 = CTkButton(master=root, corner_radius=20)

# Grid layout
button1.grid(padx=20, pady=20, row=0, column=0, sticky="nsew")
button2.grid(padx=20, pady=20, row=0, column=1, sticky="nsew")
button3.grid(padx=20, pady=20, row=0, column=2, sticky="nsew")
button4.grid(padx=20, pady=20, row=0, column=3, sticky="nsew")

padx_info = button1.grid_info()['padx']
pady_info = button1.grid_info()['pady']

# List of widgets to exclude from the count
exclude_widgets = []

# Set grid weights to make buttons resize properly
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.bind("<Configure>", lambda event: update_size(500, 200, padx_info, pady_info, exclude_widgets))
root.mainloop()