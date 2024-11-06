from main import FlexGrid
from customtkinter import *

# Set up root window, can be anything you may like
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

# Register buttons with flex_grid
flex_grid.add_widget(button1, padx=20, pady=20)
flex_grid.add_widget(button2, padx=20, pady=20)
flex_grid.add_widget(button3, padx=20, pady=20)
flex_grid.add_widget(button4, padx=20, pady=20)
flex_grid.add_widget(button5, padx=20, pady=20)
flex_grid.add_widget(button6, padx=20, pady=20)
flex_grid.add_widget(button7, padx=20, pady=20)

# sets up the flex grid parameters
flex_grid.flex_setup(minimum_width=300, 
                     minimum_height=150,  
                     flex_max=None, 
                     flex_wrap="wrap", 
                     flex_growX=2, 
                     flex_growY=2)

root.mainloop()
