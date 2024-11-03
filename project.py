

import tkinter as tk
from tkinter import messagebox

# Function to solve the Fractional Knapsack Problem
def fractional_knapsack(values, weights, capacity):
    ratios = [(values[i] / weights[i], i) for i in range(len(values))]
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    loaded_parcels = []
    
    for ratio, i in ratios:
        if weights[i] <= capacity:
            capacity -= weights[i]
            total_value += values[i]
            loaded_parcels.append((i, 1))
        else:
            fraction = capacity / weights[i]
            total_value += values[i] * fraction
            loaded_parcels.append((i, fraction))
            break

    return total_value, loaded_parcels

# Function to get input from user and solve the problem
def solve_knapsack():
    try:
        n = int(entry_parcels.get())
        if n <= 0:
            raise ValueError("Number of parcels should be positive.")

        values = [int(v) for v in entry_values.get().split()]
        weights = [int(w) for w in entry_weights.get().split()]
        capacity = int(entry_capacity.get())

        if len(values) != n or len(weights) != n:
            raise ValueError("Please enter exactly the correct number of values and weights.")

        if capacity <= 0:
            raise ValueError("Capacity should be a positive integer.")

        max_value, loaded_parcels = fractional_knapsack(values, weights, capacity)

        result_text = f"The maximum value of parcels that can be loaded is: {max_value:.2f}\n"
        result_text += "Parcels included in the optimal solution:\n"
        for i, fraction in loaded_parcels:
            result_text += f"Parcel {i + 1} with fraction {fraction:.2f}\n"
        
        result_label.config(text=result_text)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Tkinter GUI Setup
root = tk.Tk()
root.title("Parcel Logistic Optimization")
root.geometry("400x500")
root.configure(bg="#f7f7f7")

# Header Frame
header_frame = tk.Frame(root, bg="#4A90E2", padx=10, pady=10)
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

header_label = tk.Label(header_frame, text="Parcel Logistic Optimization", font=("Helvetica", 16, "bold"), fg="white", bg="#4A90E2")
header_label.pack()

# Input Frame
input_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
input_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Number of parcels input
tk.Label(input_frame, text="Number of Parcels:", font=("Arial", 10), bg="#ffffff").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_parcels = tk.Entry(input_frame, font=("Arial", 10), width=20)
entry_parcels.grid(row=0, column=1, padx=10, pady=5)

# Parcel values input
tk.Label(input_frame, text="Parcel Values (space-separated):", font=("Arial", 10), bg="#ffffff").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_values = tk.Entry(input_frame, font=("Arial", 10), width=20)
entry_values.grid(row=1, column=1, padx=10, pady=5)

# Parcel weights input
tk.Label(input_frame, text="Parcel Weights (space-separated):", font=("Arial", 10), bg="#ffffff").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_weights = tk.Entry(input_frame, font=("Arial", 10), width=20)
entry_weights.grid(row=2, column=1, padx=10, pady=5)

# Vehicle capacity input
tk.Label(input_frame, text="Vehicle Capacity (in kg):", font=("Arial", 10), bg="#ffffff").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_capacity = tk.Entry(input_frame, font=("Arial", 10), width=20)
entry_capacity.grid(row=3, column=1, padx=10, pady=5)

# Button to solve the problem
solve_button = tk.Button(root, text="Optimize Parcels", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=solve_knapsack)
solve_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

# Result Frame
result_frame = tk.Frame(root, bg="#f7f7f7", padx=10, pady=10)
result_frame.grid(row=5, column=0, columnspan=2, sticky="ew")

# Label to display the results
result_label = tk.Label(result_frame, text="", justify="left", font=("Arial", 10), bg="#f7f7f7", anchor="w")
result_label.pack(fill="both", padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()

