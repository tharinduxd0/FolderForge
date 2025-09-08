import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import json
import argparse
import sys

# --- Core Functionality --- #
def create_nested_folders(base_dir, structure, log_widget=print):
    """Recursively create folders from dict/list."""
    if isinstance(structure, dict):
        for key, value in structure.items():
            folder_path = os.path.join(base_dir, key)
            os.makedirs(folder_path, exist_ok=True)
            log_widget(f"✅ Created folder: {folder_path}")
            create_nested_folders(folder_path, value, log_widget)
    elif isinstance(structure, list):
        for item in structure:
            if isinstance(item, str):
                folder_path = os.path.join(base_dir, item)
                os.makedirs(folder_path, exist_ok=True)
                log_widget(f"✅ Created folder: {folder_path}")
            elif isinstance(item, dict):
                create_nested_folders(base_dir, item, log_widget)

# --- GUI Functions --- #
def start_creation():
    base_dir = base_dir_entry.get().strip()
    if not base_dir:
        messagebox.showerror("Error", "Please select a base directory.")
        return

    raw_text = names_textbox.get("1.0", tk.END).strip()
    if not raw_text:
        messagebox.showerror("Error", "Please enter folder names or JSON structure.")
        return

    try:
        structure = json.loads(raw_text)
    except json.JSONDecodeError:
        structure = [line.strip() for line in raw_text.splitlines() if line.strip()]

    log_box.insert(tk.END, f"Starting folder creation in: {base_dir}\n")
    create_nested_folders(base_dir, structure, log_box.insert_end)
    messagebox.showinfo("Success", "✅ Folders created successfully!")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        base_dir_entry.delete(0, tk.END)
        base_dir_entry.insert(0, folder)

def clear_log():
    log_box.delete("1.0", tk.END)

def load_template():
    selected = template_var.get()
    if selected in templates:
        names_textbox.delete("1.0", tk.END)
        names_textbox.insert(tk.END, json.dumps(templates[selected], indent=4))
        log_box.insert(tk.END, f"ℹ️ Loaded template: {selected}\n")

def export_structure():
    raw_text = names_textbox.get("1.0", tk.END).strip()
    if not raw_text:
        messagebox.showerror("Error", "Nothing to export.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(raw_text)
        log_box.insert(tk.END, f"💾 Folder structure exported to: {file_path}\n")

def import_structure():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        names_textbox.delete("1.0", tk.END)
        names_textbox.insert(tk.END, content)
        log_box.insert(tk.END, f"📂 Folder structure imported from: {file_path}\n")

# --- Treeview for Visual Builder --- #
def add_tree_folder():
    selected = tree.selection()
    if selected:
        tree.insert(selected[0], "end", text="📁 New Folder")
        log_box.insert(tk.END, "🆕 Added 'New Folder' in visual builder.\n")

def tree_to_dict(parent):
    """Convert Treeview structure to nested dict/list."""
    children = tree.get_children(parent)
    result = []
    for c in children:
        text = tree.item(c, "text").replace("📁 ", "")
        sub = tree_to_dict(c)
        if sub:
            result.append({text: sub})
        else:
            result.append(text)
    return result

def load_tree_to_text():
    structure = tree_to_dict("")
    names_textbox.delete("1.0", tk.END)
    names_textbox.insert(tk.END, json.dumps(structure, indent=4))
    log_box.insert(tk.END, "ℹ️ Loaded Treeview structure into JSON input.\n")

# --- Tkinter UI Setup --- #
if not hasattr(sys, 'argv') or len(sys.argv) == 1:  # GUI mode
    root = tk.Tk()
    root.title("FolderForge")
    root.geometry("850x700")
    root.resizable(True, True)

    # --- Base Directory --- #
    frame_top = tk.Frame(root)
    frame_top.pack(fill="x", padx=10, pady=5)
    tk.Label(frame_top, text="Base Directory:").pack(side="left")
    default_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir_entry = tk.Entry(frame_top, width=50)
    base_dir_entry.pack(side="left", padx=5)
    base_dir_entry.insert(0, default_dir)
    tk.Button(frame_top, text="Browse", command=browse_folder).pack(side="left")

    # --- Template Library --- #
    template_frame = tk.Frame(root)
    template_frame.pack(fill="x", padx=10, pady=5)
    tk.Label(template_frame, text="Template Library:").pack(side="left")
    templates = {
        "Game Levels": {
            "Level 1": ["Enemies", "Loot", "Boss"],
            "Level 2": ["Enemies", "Loot", "Boss"]
        },
        "Project Structure": {
            "src": ["components", "utils", "assets"],
            "docs": ["design", "specs"]
        }
    }
    template_var = tk.StringVar()
    template_var.set("Select template")
    tk.OptionMenu(template_frame, template_var, *templates.keys()).pack(side="left", padx=5)
    tk.Button(template_frame, text="Load Template", command=load_template).pack(side="left", padx=5)

    # --- Names / nested structure input --- #
    tk.Label(root, text="Folder Names / JSON Structure:").pack(anchor="w", padx=10)
    names_textbox = scrolledtext.ScrolledText(root, height=12)
    names_textbox.pack(fill="both", expand=True, padx=10, pady=5)
    # Example placeholder
    example_json = {
        "Ashina Outskirts": ["General Naomori Kawarada","Chained Ogre","Gyoubu Masataka Oniwa"],
        "Ashina Depths": ["Mist Noble","O'Rin of the Water","Corrupted Monk (illusion)"]
    }
    names_textbox.insert(tk.END, json.dumps(example_json, indent=4))

    # --- Treeview Builder --- #
    tree_frame = tk.Frame(root)
    tree_frame.pack(fill="both", expand=True, padx=10, pady=5)
    tk.Label(tree_frame, text="Visual Folder Builder:").pack(anchor="w")
    tree = ttk.Treeview(tree_frame)
    tree.pack(fill="both", expand=True)
    root_node = tree.insert("", "end", text="📁 Base Folder", open=True)
    tk.Button(tree_frame, text="Add Folder", command=add_tree_folder).pack(pady=5)
    tk.Button(tree_frame, text="Load Tree → JSON", command=load_tree_to_text).pack(pady=5)

    # --- Buttons --- #
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=5)
    tk.Button(frame_buttons, text="Create Folders", command=start_creation, bg="#4CAF50", fg="white").pack(side="left", padx=5)
    tk.Button(frame_buttons, text="Clear Log", command=clear_log, bg="#f44336", fg="white").pack(side="left", padx=5)
    tk.Button(frame_buttons, text="Export Config", command=export_structure).pack(side="left", padx=5)
    tk.Button(frame_buttons, text="Import Config", command=import_structure).pack(side="left", padx=5)

    # --- Log area --- #
    tk.Label(root, text="Folder creation log:").pack(anchor="w", padx=10)
    log_box = scrolledtext.ScrolledText(root, height=12, state="normal")
    log_box.pack(fill="both", expand=True, padx=10, pady=5)
    log_box.insert(tk.END, "ℹ️ Enter folder names line-by-line or JSON structure.\n")

    # Add method to insert log text
    def insert_end(msg):
        log_box.insert(tk.END, msg + "\n")
        log_box.see(tk.END)
    log_box.insert_end = insert_end

    root.mainloop()

# --- CLI Mode --- #
else:
    parser = argparse.ArgumentParser(description="FolderForge CLI")
    parser.add_argument("base_dir", help="Base directory path")
    parser.add_argument("structure_file", help="JSON file with folder structure")
    args = parser.parse_args()
    with open(args.structure_file, "r") as f:
        structure = json.load(f)
    create_nested_folders(args.base_dir, structure, log_widget=print)
