import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ParaV!ru$ File Search")

        self.label = tk.Label(root, text="Enter the filename:")
        self.label.pack()

        self.filename_entry = tk.Entry(root)
        self.filename_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_file)
        self.search_button.pack()

        self.result_text = tk.Text(root, height=10, width=40)
        self.result_text.pack()

    def search_file(self):
        target_filename = self.filename_entry.get()
        if not target_filename:
            messagebox.showerror("Error", "Please enter a filename.")
            return

        found_paths = self.find_files(target_filename)

        if found_paths:
            self.result_text.delete('1.0', tk.END)  # Clear previous results
            for path in found_paths:
                self.result_text.insert(tk.END, f"File '{target_filename}' found at:\n{path}\n\n")
        else:
            messagebox.showinfo("File Not Found", f"File '{target_filename}' not found in any directory and its subdirectories.")

    def find_files(self, filename):
        found_paths = []
        for root, dirs, files in os.walk('/'):
            if filename in files:
                found_paths.append(os.path.join(root, filename))
        return found_paths

def main():
    root = tk.Tk()
    app = FileSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
