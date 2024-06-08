import tkinter as tk
from tkinter import messagebox

entries = {}  # Define entries dictionary here


def calculate_rank():
    # Get matrix dimensions
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())

    # Get matrix elements
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            entry = entries[(i, j)].get()
            if entry.strip() == "":
                messagebox.showerror("Error", "Please fill in all matrix elements")
                return
            row.append(int(entry))
        matrix.append(row)

    # Calculate rank
    rank = calculateRank(matrix)

    # Display rank
    rank_label.config(text="The rank of the matrix is: " + str(rank))


def calculateRank(matrix):
    rank = 0
    rowCount = len(matrix)
    colCount = len(matrix[0])
    minDim = min(rowCount, colCount)

    for i in range(minDim):
        if matrix[i][i] != 0:
            rank += 1
            for j in range(i + 1, rowCount):
                multiplier = matrix[j][i] / matrix[i][i]
                for k in range(i, colCount):
                    matrix[j][k] -= multiplier * matrix[i][k]
        else:
            reduce = True
            for j in range(i + 1, rowCount):
                if matrix[j][i] != 0:
                    swapRows(matrix, i, j)
                    reduce = False
                    break
            if reduce:
                rank -= 1
                for j in range(i, rowCount):
                    matrix[j][i] = matrix[j][colCount - 1]
            i -= 1

    return rank


def swapRows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def create_matrix_entry_widgets():
    # Clear previous widgets if any
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    # Create entry widgets for matrix elements
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    for i in range(rows):
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            entries[(i, j)] = entry


# Create tkinter window
root = tk.Tk()
root.title("Matrix Rank Calculator")

# Create labels and entries for matrix dimensions
rows_label = tk.Label(root, text="Enter the number of rows in the matrix:")
rows_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
rows_entry = tk.Entry(root)
rows_entry.grid(row=0, column=1, padx=10, pady=5)

cols_label = tk.Label(root, text="Enter the number of columns in the matrix:")
cols_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
cols_entry = tk.Entry(root)
cols_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to create entry widgets for matrix elements
create_button = tk.Button(root, text="Create Matrix", command=create_matrix_entry_widgets)
create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Frame to hold matrix entry widgets
matrix_frame = tk.Frame(root)
matrix_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Button to calculate rank
calculate_button = tk.Button(root, text="Calculate Rank", command=calculate_rank)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Label to display rank
rank_label = tk.Label(root, text="")
rank_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
