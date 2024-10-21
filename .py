import tkinter as tk
from tkinter import filedialog, Text
from tkinter import messagebox

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
        root.title(f"Notepad - {file_path}")

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        root.title(f"Notepad - {file_path}")

# Function to create a new file
def new_file():
    if messagebox.askyesno("New File", "Unsaved work will be lost. Do you want to continue?"):
        text_area.delete(1.0, tk.END)
        root.title("Notepad - New File")

# Function to exit the notepad
def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Create the text area
text_area = Text(root, font=("Arial", 12))
text_area.pack(fill=tk.BOTH, expand=True)

# Create the menu bar
menu_bar = tk.Menu(root)

# Add "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command.save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

# Display the menu bar
root.config(menu=menu_bar)

# Start the application
root.mainloop()
