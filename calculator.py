import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x500+450+500")  # Width x Height + X_Offset + Y_Offset

# Create an entry widget for input
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create number and operator buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack(fill=tk.BOTH, expand=True)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0

for button_text in buttons:
    if button_text == '=':
        button = tk.Button(buttons_frame, text=button_text, padx=20, pady=20, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(buttons_frame, text=button_text, padx=20, pady=20, font=("Arial", 18), command=lambda text=button_text: button_click(text))
    
    button.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure row and column weights for resizing
for i in range(4):
    buttons_frame.grid_rowconfigure(i, weight=1)
    buttons_frame.grid_columnconfigure(i, weight=1)

# Start the Tkinter main loop
root.mainloop()
