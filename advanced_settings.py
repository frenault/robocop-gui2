import tkinter as tk
from tkinter import ttk

# Define all Robocopy flags with descriptions
ROBOCOPY_FLAGS = {
    "/S": "Copy subdirectories (excluding empty ones)",
    "/E": "Copy subdirectories (including empty ones)",
    "/Z": "Copy files in restartable mode",
    "/PURGE": "Delete destination files and directories not present in the source",
    "/MIR": "Mirror directory tree (equivalent to /E and /PURGE)",
    "/R:n": "Number of retries on failed copies (default is 1 million)",
    "/W:n": "Wait time between retries (default is 30 seconds)",
    "/MT[:n]": "Multi-threaded copying with n threads (default is 8)",
    "/LOG:file": "Output log file",
    "/LOG+:file": "Append to log file",
    "/NP": "No progress output during copy",
    "/MOVE": "Move files and directories (delete from source)",
    "/COPYALL": "Copy all file information",
    "/SEC": "Copy files with security (ACLs)",
    "/DCOPY:T": "Copy directory timestamps",
    "/TIMFIX": "Fix file times on all copies",
    "/XO": "Exclude older files",
    "/XD": "Exclude directories matching the names",
    "/XF": "Exclude files matching the names"
    # Add additional flags as needed
}

def show_advanced_settings(root):
    # Create advanced settings window
    advanced_window = tk.Toplevel(root)
    advanced_window.title("Advanced Settings")
    advanced_window.geometry("900x500")
    advanced_window.configure(bg="#ffffff")

    # Add title label
    tk.Label(
        advanced_window,
        text="Advanced Settings (Enable/Disable and Editable Values)",
        font=("Segoe UI", 14, "bold"),
        bg="#ffffff",
        fg="#333333"
    ).pack(pady=10)

    # Create Treeview (Excel-like table)
    columns = ("Enabled", "Flag", "Description", "Value")
    tree = ttk.Treeview(advanced_window, columns=columns, show="headings", height=15)
    tree.heading("Enabled", text="Enabled")
    tree.heading("Flag", text="Flag")
    tree.heading("Description", text="Description")
    tree.heading("Value", text="Value")

    tree.column("Enabled", width=100, anchor="center")
    tree.column("Flag", width=150, anchor="w")
    tree.column("Description", width=450, anchor="w")
    tree.column("Value", width=150, anchor="w")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Populate Treeview with Robocopy flags
    for flag, description in ROBOCOPY_FLAGS.items():
        tree.insert("", tk.END, values=("False", flag, description, ""))

    # Allow users to edit the "Value" column
    def on_double_click(event):
        item_id = tree.identify_row(event.y)
        column_id = tree.identify_column(event.x)
        if not item_id or column_id not in ("#1", "#4"):
            return  # Only allow editing in "Enabled" and "Value" columns

        # If "Enabled" column (toggle checkbox)
        if column_id == "#1":
            current_value = tree.item(item_id, "values")[0]
            new_value = "True" if current_value == "False" else "False"
            tree.set(item_id, column="Enabled", value=new_value)

        # If "Value" column (edit value)
        elif column_id == "#4":
            # Get current cell coordinates
            bbox = tree.bbox(item_id, column_id)
            x, y, w, h = bbox
            entry_popup = tk.Entry(advanced_window)
            entry_popup.insert(0, tree.set(item_id, "Value"))
            entry_popup.place(x=x + 15, y=y + 10, width=w, height=h)
            entry_popup.focus_set()

            def save_value():
                tree.set(item_id, "Value", entry_popup.get())
                entry_popup.destroy()

            entry_popup.bind("<Return>", lambda _: save_value())
            entry_popup.bind("<FocusOut>", lambda _: save_value())

    tree.bind("<Double-1>", on_double_click)

    # Function to save settings
    def save_settings():
        selected_flags = []
        for item in tree.get_children():
            values = tree.item(item, "values")
            enabled = values[0] == "True"  # Check if enabled
            flag = values[1]
            value = values[3]
            if enabled:  # Only include enabled flags
                if value.strip():
                    selected_flags.append(f"{flag}{value}")
                else:
                    selected_flags.append(flag)
        advanced_window.selected_flags = selected_flags
        advanced_window.destroy()

    # Save button
    tk.Button(
        advanced_window,
        text="Save",
        font=("Segoe UI", 12, "bold"),
        bg="#0078D7",
        fg="#ffffff",
        command=save_settings
    ).pack(pady=10)

    advanced_window.selected_flags = []

# Example for testing the window independently (comment this out for production use)
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_advanced_settings(root)
    root.mainloop()
