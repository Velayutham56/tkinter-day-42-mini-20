from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Temperature Converter")

def convert_temp(event=None):
    try:
        temp = float(temp_spin.get())
        unit = unit_combo.get()
        if unit == "Celsius":
            converted = (temp * 9/5) + 32
            result_label.config(text=f"{converted:.2f} °F")
        else:
            converted = (temp - 32) * 5/9
            result_label.config(text=f"{converted:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input")

# Temperature input
temp_spin = Spinbox(root, from_=-100, to=100)
temp_spin.pack(pady=5)
temp_spin.bind("<KeyRelease>", convert_temp)
temp_spin.bind("<ButtonRelease-1>", convert_temp)

# Unit selection
unit_combo = ttk.Combobox(root, values=["Celsius", "Fahrenheit"])
unit_combo.set("Select Unit")
unit_combo.pack(pady=5)
unit_combo.bind("<<ComboboxSelected>>", convert_temp)

# Convert Button
Button(root, text="Convert", command=convert_temp).pack(pady=5)

# Result display
result_label = Label(root, text="Result will appear here")
result_label.pack(pady=5)

root.mainloop()
