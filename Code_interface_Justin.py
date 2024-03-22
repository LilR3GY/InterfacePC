import tkinter as tk
from tkinter import ttk, filedialog, StringVar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Constants for unit conversion
GRAMS_TO_OUNCES = 0.035274

def plot_graph():
    # Create data
    x = np.linspace(0, 10, 100)
    y = 4*np.sin(4*x)+50
    
    # Apply unit conversion if set to ounces
    if unit_option.get() == "oz":
        y *= GRAMS_TO_OUNCES
        ylabel = 'Poids (oz)'
        
        # Set Y-axis limits specific to ounces
        y_limits = (-0.8, 4)
    else:
        ylabel = 'Poids (g)'
        
        # Set default Y-axis limits for grams
        y_limits = (-20, 110)

    # Clear previous plot
    ax.clear()

    # Plot new data
    ax.plot(x, y)
    ax.set_xlabel('Temps (s)')
    ax.set_ylabel(ylabel)
    ax.set_title('Poids sur la balance en fonction du temps')

    # Set Y-axis limits
    ax.set_ylim(y_limits)

    # Calculate and update average label
    update_average_label(y)

    # Update stability label
    update_stability_label(y)

    # Refresh canvas
    canvas.draw()


def zero_graph():
    # Get the current Y-axis values
    y_data = ax.get_lines()[0].get_ydata()
    
    # Calculate the average of the last 10 Y-axis values
    last_10_values = y_data[-10:]
    average_value = np.mean(last_10_values)
    
    # Subtract the average from all Y-axis values
    y_data -= average_value
    
    # Update the plot with the new Y-axis values
    ax.clear()
    ax.plot(np.linspace(0, 10, len(y_data)), y_data)
    ax.set_xlabel('Temps (s)')
    
    # Apply unit conversion if set to ounces
    if unit_option.get() == "oz":
        y_data *= GRAMS_TO_OUNCES
        ax.set_ylabel('Temps (oz)')
    else:
        ax.set_ylabel('Poids (g)')
    
    ax.set_title('Poids sur la balance en fonction du temps')

    # Calculate and update average label
    update_average_label(y_data)

    # Update stability label
    update_stability_label(y_data)

    # Set Y-axis limits
    ax.set_ylim(-20, 110)

    # Refresh canvas
    canvas.draw()

def divide_by_factor(factor):
    if ax.lines:
        # Get the current Y-axis values
        y_data = ax.lines[0].get_ydata()
        
        # Calculate the average of the last 10 Y-axis values
        last_10_values = y_data[-10:]
        average_value = np.mean(last_10_values)
        
        # Divide the average by the specified factor
        result = average_value / factor
        
        # Update the label with the result
        function_label.config(text=f"Nombre de pièce : {int(round(result))}")
    else:
        # Handle the case when there are no lines in the plot
        function_label.config(text="No data to divide. Plot the graph first.")

def reset_graph():
    # Clear previous plot
    ax.clear()
    # Set Y-axis limits
    ax.set_ylim(-20, 110)
    # Refresh canvas
    canvas.draw()

def update_average_label(y):
    # Update average label with the average of last 10 y values
    last_10_values = y[-10:]
    average_value = np.mean(last_10_values)
    if unit_option.get() == "oz":
        average_value *= GRAMS_TO_OUNCES
        average_label.config(text=f'Masse mesurée : {average_value:.2f} oz')
    else:
        average_label.config(text=f'Masse mesurée : {average_value:.2f} g')

def update_stability_label(y):
    # Update stability label based on the stability of the last 10 values
    if len(y) >= 10:
        deviation = np.std(y[-10:]) / np.mean(y[-10:])
        if deviation <= 0.05:
            stability_label.config(text='Stable', foreground='green')
        else:
            stability_label.config(text='Not Stable', foreground='red')

def save_plot():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
    if file_path:
        fig.savefig(file_path)

# Create Tkinter window
root = tk.Tk()
root.title("Weight Graph")

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create Matplotlib figure and axes
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a frame for buttons and labels
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.LEFT, fill=tk.Y)

# Create label for displaying average
average_label = ttk.Label(control_frame, text='')
average_label.pack(side=tk.TOP, padx=5, pady=5)

# Create label for displaying stability
stability_label = ttk.Label(control_frame, text='Stable', foreground='green')
stability_label.pack(side=tk.TOP, padx=5, pady=5)

# Create buttons
plot_button = ttk.Button(control_frame, text="Plot", command=plot_graph)
plot_button.pack(side=tk.TOP, padx=5, pady=5)

zero_button = ttk.Button(control_frame, text="Zero", command=zero_graph)
zero_button.pack(side=tk.TOP, padx=5, pady=5)

reset_button = ttk.Button(control_frame, text="Reset", command=reset_graph)
reset_button.pack(side=tk.TOP, padx=5, pady=5)

save_button = ttk.Button(control_frame, text="Save Plot", command=save_plot)
save_button.pack(side=tk.TOP, padx=5, pady=5)

# Create a frame for function option menu
function_frame = ttk.Frame(control_frame)
function_frame.pack(side=tk.TOP, padx=5, pady=5)

# Create function option menu
functions = [('Pièce de 1 dollar', 7.3), ('Pièce de 2 dollars', 7), ('Pièce de 25 cents', 5), ('Pièce de 10 cents', 2.07), ('Pièce de 5 cents', 4.6)]
selected_factor = tk.StringVar()
selected_factor.set(functions[0][0])  # Set default value
function_option_menu = ttk.OptionMenu(function_frame, selected_factor, functions[0][0], *[item[0] for item in functions], command=lambda x: divide_by_factor(next(item[1] for item in functions if item[0] == x)))
function_option_menu.pack(padx=5, pady=5)

# Create label for displaying function result
function_label = ttk.Label(control_frame, text='')
function_label.pack(side=tk.TOP, padx=5, pady=5)

# Create unit option menu
unit_option = StringVar()
unit_option.set("g")  # Default unit is grams
unit_menu = ttk.OptionMenu(control_frame, unit_option, "g", "g", "oz")
unit_menu.pack(side=tk.TOP, padx=5, pady=5)

# Define function_option_menu as a global variable
function_option_menu = None

def create_function_option_menu():
    global function_option_menu
    global functions
    selected_factor.set(functions[0][0])
    function_option_menu = ttk.OptionMenu(function_frame, selected_factor, functions[0][0], *[item[0] for item in functions], command=lambda x: divide_by_factor(next(item[1] for item in functions if item[0] == x)))
    function_option_menu.pack(padx=5, pady=5)

def update_function_option_menu():
    global function_option_menu
    global functions
    function_option_menu.destroy()
    selected_factor.set(functions[0][0])
    function_option_menu = ttk.OptionMenu(function_frame, selected_factor, functions[0][0], *[item[0] for item in functions], command=lambda x: divide_by_factor(next(item[1] for item in functions if item[0] == x)))
    function_option_menu.pack(padx=5, pady=5)

def update_factors(unit):
    global function_option_menu
    global functions
    if unit == "oz":
        for i in range(len(functions)):
            functions[i] = (functions[i][0], functions[i][1] * GRAMS_TO_OUNCES)
    else:
        # Reset factors to their original values
        functions = [('Pièce de 1 dollar', 7.3), ('Pièce de 2 dollars', 7), ('Pièce de 25 cents', 5), ('Pièce de 10 cents', 2.07), ('Pièce de 5 cents', 4.6)]

    if function_option_menu:
        update_function_option_menu()
    else:
        create_function_option_menu()

# Callback function for unit selection
def unit_change_callback(*args):
    unit = unit_option.get()
    update_factors(unit)
    plot_graph()

# Set trace on the unit_option variable to call unit_change_callback when the option is changed
unit_option.trace_add("write", unit_change_callback)

# Create a Text widget for command input
command_entry = tk.Text(control_frame, height=4, width=50)
command_entry.pack(side=tk.TOP, padx=5, pady=5)

def execute_command():
    command = command_entry.get("1.0", tk.END).strip()
    # Execute the command (you can define the execution logic here)
    print("Command:", command)

# Create a button to execute the command
execute_button = ttk.Button(control_frame, text="Execute Command", command=execute_command)
execute_button.pack(side=tk.TOP, padx=5, pady=5)

# Start Tkinter event loop
root.mainloop()
