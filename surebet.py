import tkinter as tk
from tkinter import ttk, messagebox

def calculate_surebet():
    try:
        # Get bankroll
        bankroll = float(bankroll_entry.get())
        if bankroll <= 0:
            raise ValueError("Bankroll must be greater than 0.")

        # Get number of outcomes
        num_outcomes = int(outcome_choice.get())
        odds = []

        # Get odds inputs
        for i in range(num_outcomes):
            odd = float(odds_entries[i].get())
            if odd <= 0:
                raise ValueError("Odds must be greater than 0.")
            odds.append(odd)

        # Calculate total probability
        total_probability = sum(1 / odd for odd in odds)

        if total_probability >= 1:
            messagebox.showerror("Error", "This is not a surebet.")
            return

        # Calculate stakes
        stakes = [(bankroll / (odd * total_probability)) for odd in odds]

        # Calculate guaranteed profit
        profits = [stake * odd - bankroll for stake, odd in zip(stakes, odds)]
        guaranteed_profit = min(profits)

        # Calculate arbitrage percentage
        arbitrage_percentage = (1 - total_probability) * 100

        # Display results
        results_text.set(
            f"Arbitrage Percentage: {arbitrage_percentage:.2f}%\n"
            f"Guaranteed Profit: ${guaranteed_profit:.2f}\n"
            + "\n".join(
                [f"Stake on Outcome {i+1}: ${stakes[i]:.2f}" for i in range(num_outcomes)]
            )
        )
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {str(e)}")

def update_odds_entries(*args):
    # Update the number of odds entry fields based on selection
    num_outcomes = int(outcome_choice.get())
    for i in range(10):
        if i < num_outcomes:
            odds_labels[i].grid(row=i + 3, column=0, pady=5, sticky="e")
            odds_entries[i].grid(row=i + 3, column=1, pady=5)
        else:
            odds_labels[i].grid_remove()
            odds_entries[i].grid_remove()

# Create the main Tkinter window
root = tk.Tk()
root.title("Surebet Calculator")
root.configure(bg="gray")

# Variables
outcome_choice = tk.StringVar(value="2")
results_text = tk.StringVar()

# Title Label
tk.Label(root, text="Surebet Calculator", bg="gray", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Bankroll Entry
tk.Label(root, text="Bankroll:", bg="gray", fg="white", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
bankroll_entry = tk.Entry(root, font=("Arial", 12))
bankroll_entry.grid(row=1, column=1, pady=5)

# Outcome Selection
tk.Label(root, text="Number of Outcomes:", bg="gray", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="e")
outcome_dropdown = ttk.Combobox(root, textvariable=outcome_choice, values=[str(i) for i in range(2, 11)], state="readonly", font=("Arial", 12))
outcome_dropdown.grid(row=2, column=1, pady=5)
outcome_dropdown.bind("<<ComboboxSelected>>", update_odds_entries)

# Odds Input Fields
odds_labels = []
odds_entries = []

for i in range(10):
    label = tk.Label(root, text=f"Odds for Outcome {i + 1}:", bg="gray", fg="white", font=("Arial", 12))
    entry = tk.Entry(root, font=("Arial", 12))
    odds_labels.append(label)
    odds_entries.append(entry)

update_odds_entries()  # Initialize the first two fields

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_surebet, font=("Arial", 12, "bold"), bg="green", fg="white")
calculate_button.grid(row=13, column=0, columnspan=2, pady=10)

# Results Display
results_label = tk.Label(root, textvariable=results_text, bg="gray", fg="white", font=("Arial", 12), justify="left")
results_label.grid(row=14, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()

