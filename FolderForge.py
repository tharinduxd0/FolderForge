import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import json

def create_nested_folders(base_dir, structure, log_widget):
    """Recursively creates nested folders from dict or list."""
    if isinstance(structure, dict):
        for key, value in structure.items():
            area_path = os.path.join(base_dir, key)
            os.makedirs(area_path, exist_ok=True)
            log_widget.insert(tk.END, f"✅ Created folder: {area_path}\n")
            create_nested_folders(area_path, value, log_widget)
    elif isinstance(structure, list):
        for item in structure:
            if isinstance(item, str):
                folder_path = os.path.join(base_dir, item)
                os.makedirs(folder_path, exist_ok=True)
                log_widget.insert(tk.END, f"✅ Created folder: {folder_path}\n")
            elif isinstance(item, dict):
                create_nested_folders(base_dir, item, log_widget)

def start_creation():
    base_dir = base_dir_entry.get().strip()
    if not base_dir:
        messagebox.showerror("Error", "Please select a base directory.")
        return

    raw_text = names_textbox.get("1.0", tk.END).strip()
    if not raw_text:
        messagebox.showerror("Error", "Please enter folder names or nested JSON structure.")
        return

    try:
        structure = json.loads(raw_text)
    except json.JSONDecodeError:
        structure = [line.strip() for line in raw_text.splitlines() if line.strip()]

    log_box.insert(tk.END, f"Starting folder creation in: {base_dir}\n")
    create_nested_folders(base_dir, structure, log_box)
    messagebox.showinfo("Success", "✅ Folders created successfully!")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        base_dir_entry.delete(0, tk.END)
        base_dir_entry.insert(0, folder)

def clear_log():
    log_box.delete("1.0", tk.END)

# --- UI Setup ---
root = tk.Tk()
root.title("FolderForge")
root.geometry("750x650")
root.resizable(True, True)

# --- Base Directory --- #
frame_top = tk.Frame(root)
frame_top.pack(fill="x", padx=10, pady=5)

tk.Label(frame_top, text="Base Directory:").pack(side="left")

# Default base directory: same folder as script
default_dir = os.path.dirname(os.path.abspath(__file__))
base_dir_entry = tk.Entry(frame_top, width=50)
base_dir_entry.pack(side="left", padx=5)
base_dir_entry.insert(0, default_dir)

browse_btn = tk.Button(frame_top, text="Browse", command=browse_folder)
browse_btn.pack(side="left")

# --- Names / nested structure input --- #
tk.Label(root, text="Enter folder names (one per line) or JSON nested structure:").pack(anchor="w", padx=10)
names_textbox = scrolledtext.ScrolledText(root, height=15)
names_textbox.pack(fill="both", expand=True, padx=10, pady=5)

# Placeholder example
example_json = {
    "Ashina Outskirts": [
        "General Naomori Kawarada",
        "Chained Ogre",
        "Gyoubu Masataka Oniwa"
    ],
    "Ashina Depths": [
        "Mist Noble",
        "O'Rin of the Water",
        "Corrupted Monk (illusion)"
    ]
}
names_textbox.insert(tk.END, "# Example JSON placeholder:\n")
names_textbox.insert(tk.END, json.dumps(example_json, indent=4))
names_textbox.insert(tk.END, "\n# You can also enter plain names line-by-line.\n")

# --- Buttons --- #
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

create_btn = tk.Button(frame_buttons, text="Create Folders", command=start_creation,
                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
create_btn.pack(side="left", padx=5)

clear_log_btn = tk.Button(frame_buttons, text="Clear Log", command=clear_log,
                          bg="#f44336", fg="white", font=("Arial", 12, "bold"))
clear_log_btn.pack(side="left", padx=5)

# --- Log area --- #
tk.Label(root, text="Folder creation log:").pack(anchor="w", padx=10)
log_box = scrolledtext.ScrolledText(root, height=12, state="normal")
log_box.pack(fill="both", expand=True, padx=10, pady=5)

# Info / guidance messages
log_box.insert(tk.END, "ℹ️ Base directory defaults to script location, but you can change it.\n")
log_box.insert(tk.END, "ℹ️ You can enter folder names line-by-line or nested JSON format.\n")
log_box.insert(tk.END, "ℹ️ JSON keys become parent folders, lists become subfolders.\n")
log_box.insert(tk.END, "ℹ️ Example JSON is preloaded above as a reference.\n")

root.mainloop()
