import tkinter as tk

def plus():
    value = int(label_value["text"])
    label_value["text"] = f"{value + 1}"


def minus():
    value = int(label_value["text"])
    label_value["text"] = f"{value - 1}"

# Created window
window = tk.Tk()
window.title("Enter Year of Birth")

# Format Window
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# Create Left Button (subtract)
button_minus = tk.Button(text="-", command=minus)
button_minus.grid(row=0, column=0, sticky="nsew")

# Create Label
label_value = tk.Label(text="0")
label_value.grid(row=0, column=1)

# Create Right Button (add)
button_plus = tk.Button(text="+", command=plus)
button_plus.grid(row=0, column=2, sticky="nsew")

window.mainloop()
