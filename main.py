import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import robocopy_logic
import advanced_settings

def browse_directory(entry):
    directory = filedialog.askdirectory()
    if directory:
        entry.delete(0, tk.END)
        entry.insert(0, directory)

def start_robocopy():
    source = source_entry.get()
    destination = dest_entry.get()
    if not source or not destination:
        log_text.insert(tk.END, "Source and Destination are required!\n", "error")
        return
    robocopy_logic.start_robocopy(source, destination, log_text, progress_var)

def stop_robocopy():
    robocopy_logic.stop_robocopy(log_text)

def save_settings():
    robocopy_logic.save_settings(source_entry.get(), dest_entry.get())
    log_text.insert(tk.END, "Settings saved!\n", "success")

def show_advanced_settings():
    advanced_settings.show_advanced_settings(root)

# Load previous config
defaults = robocopy_logic.load_config()

# GUI Setup
root = tk.Tk()
root.title("Robocopy GUI")
root.geometry("1024x768")
root.configure(bg="#ffffff")
root.resizable(True, True)

def create_label(parent, text):
    return tk.Label(parent, text=text, font=("Segoe UI", 12), bg="#ffffff", fg="#333333")

def create_entry(parent):
    return tk.Entry(parent, width=60, font=("Segoe UI", 12), bd=2, relief=tk.SOLID)

def create_button(parent, text, command, color="#0078D7"):
    return tk.Button(parent, text=text, font=("Segoe UI", 12, "bold"), bg=color, fg="white", command=command, bd=0, padx=10, pady=5, activebackground="#005bb5")

main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(padx=20, pady=20)

# Source Folder
source_frame = tk.Frame(main_frame, bg="#ffffff")
source_frame.pack(fill=tk.X, pady=5)
create_label(source_frame, "Source Folder:").pack(side=tk.LEFT, padx=5)
source_entry = create_entry(source_frame)
source_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
create_button(source_frame, "Browse", lambda: browse_directory(source_entry)).pack(side=tk.LEFT, padx=5)

# Destination Folder
dest_frame = tk.Frame(main_frame, bg="#ffffff")
dest_frame.pack(fill=tk.X, pady=5)
create_label(dest_frame, "Destination Folder:").pack(side=tk.LEFT, padx=5)
dest_entry = create_entry(dest_frame)
dest_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
create_button(dest_frame, "Browse", lambda: browse_directory(dest_entry)).pack(side=tk.LEFT, padx=5)

# Progress Bar
progress_var = tk.IntVar()
progress_frame = tk.Frame(main_frame, bg="#ffffff")
progress_frame.pack(fill=tk.X, pady=10)
progress_bar = ttk.Progressbar(progress_frame, variable=progress_var, maximum=100, length=600)
progress_bar.pack(fill=tk.X, padx=5)

# Buttons
btn_frame = tk.Frame(main_frame, bg="#ffffff")
btn_frame.pack(pady=10)
create_button(btn_frame, "Start Copy", start_robocopy).pack(side=tk.LEFT, padx=5)
create_button(btn_frame, "Stop Copy", stop_robocopy, color="#D9534F").pack(side=tk.LEFT, padx=5)
create_button(btn_frame, "Save Settings", save_settings).pack(side=tk.LEFT, padx=5)
create_button(btn_frame, "Advanced Settings", show_advanced_settings).pack(side=tk.LEFT, padx=5)

# Log Output
log_label = create_label(main_frame, "Log Output:")
log_label.pack(pady=5)
log_text = scrolledtext.ScrolledText(main_frame, width=80, height=10, font=("Consolas", 10), bg="#f9f9f9", fg="#333333", bd=2, relief=tk.SOLID)
log_text.pack(pady=5)
log_text.tag_config("info", foreground="blue")
log_text.tag_config("error", foreground="red")
log_text.tag_config("success", foreground="green")

# Copied Files
file_list_label = create_label(main_frame, "Copied Files:")
file_list_label.pack(pady=5)
file_list = ttk.Treeview(main_frame, columns=("Filename"), show="headings", height=8)
file_list.heading("Filename", text="Filename")
file_list.pack(fill=tk.BOTH, expand=True)

root.mainloop()
