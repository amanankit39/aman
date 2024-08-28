import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
create_task = []

# Set up the main window properties
root.geometry("500x600")
root.title("To-Do List")
root.config(bg="#FFDAB9")
root.iconbitmap('favicon.ico')

# Load and display an image
image = Image.open(r"C:\Users\ADITYA\Documents\__CodSoft\to-do-list.png")
resized_image = image.resize((300, 250))
image_tk = ImageTk.PhotoImage(resized_image)
image_label = tk.Label(root, image=image_tk)
image_label.pack(pady=(10, 25))

# Function to handle task entry and display a message box
def on_enter(event):
    task = task_input.get().strip()  # Get and strip any leading/trailing whitespace
    if task:  # Check if the input is not empty
        create_task.append(task)  # Add task to the list
        task_input.delete(0, tk.END)  # Clear the input field
        messagebox.showinfo("Task Saved", "Task Saved Successfully!!!")  # Show success message
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")  # Show warning for empty input
    return "break"  # Prevent further processing of the event

# Function to open a window for creating a new task
def handle_create_task():
    task_window = tk.Toplevel()  # Create a new top-level window
    task_window.geometry("500x300")
    task_window.config(bg="#FFDAB9")
    task_window.title("Create Task")
    task_window.iconbitmap('favicon.ico')

    # Create and display a heading label
    heading = tk.Label(task_window, text="Create Task", bg="#FFDAB9", fg="black")
    heading.pack(pady=(10, 15))
    heading.config(font=("helvetica", 16, "bold"))

    # Create an input field for entering tasks
    global task_input
    task_input = tk.Entry(task_window, width=60)
    task_input.pack(pady=(10, 15))
    task_input.focus_set()  # Set focus to the input field
    task_input.bind("<Return>", on_enter)  # Bind the Enter key to the on_enter function

# Button to open the task creation window
create_task_btn = tk.Button(root, text="Create Task", bg="#FF6F61", fg="black", height=3, width=50, command=handle_create_task)
create_task_btn.pack(pady=(10, 10))

# Function to display a window with the list of saved tasks
def handle_saved_task():
    saved_task_window = tk.Toplevel()  # Create a new top-level window
    saved_task_window.geometry("500x300")
    saved_task_window.config(bg="#FFDAB9")
    saved_task_window.title("Saved Task")
    saved_task_window.iconbitmap('favicon.ico')

    # Create and display a label for each saved task
    for idx, task in enumerate(create_task):
        task_label = tk.Label(saved_task_window, text=f"{idx + 1}. {task}")
        task_label.pack(pady=(10, 10))

# Button to open the window with saved tasks
saved_task_btn = tk.Button(root, text="Saved Task", bg="#FF6F61", fg="black", height=3, width=50, command=handle_saved_task)
saved_task_btn.pack(pady=(10, 10))

# Start the Tkinter event loop
root.mainloop()
