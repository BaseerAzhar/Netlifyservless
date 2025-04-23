import tkinter as tk
from tkinter import messagebox
import subprocess
import os


# Function to run the test case using pytest
def run_test_case():
    # Specify the path to your test case (e.g., test_case_1.py)
    test_script = "tests/test_case_1.py"  # Adjust the path as necessary

    try:
        # Run the test case using subprocess
        result = subprocess.run(['pytest', test_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # If the test case ran successfully
        if result.returncode == 0:
            messagebox.showinfo("Test Result", f"Test Passed!\n\n{result.stdout}")
        else:
            messagebox.showerror("Test Result", f"Test Failed!\n\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create the main window
root = tk.Tk()
root.title("Test Case Runner")
root.geometry("300x150")  # Window size

# Create a label to display instructions
label = tk.Label(root, text="Click to run Test Case 1", font=("Helvetica", 14))
label.pack(pady=20)

# Create a button to trigger the test case
run_button = tk.Button(root, text="Run Test Case 1", font=("Helvetica", 12), command=run_test_case)
run_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
