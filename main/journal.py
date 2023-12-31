import tkinter as tk
import datetime as dt
import db
import os
import constants as cons

# Initialize database.
data = db.DB()
# Hold the last entry selection.
selection: str | None = None

def refresh() -> None:
    sidebar.delete(0, tk.END)

    for path in data.entries.values():
        sidebar.insert(tk.END, path)

def get_now_str() -> str:
    now: dt.datetime = dt.datetime.now()
    return "".join([now.strftime("%a--%d-%m-%Y--%I-%M-%S-%f")[:-2], now.strftime("-%p")])

def add_entry(_) -> None:
    data.add_entry(len(data.entries), path=get_now_str())
    refresh()

def delete_entry(_) -> None:
    data.remove_entry(del_entry.get().strip())
    refresh()

def update_selection(_):
    global selection

    all_items = sidebar.get(0, tk.END)
    sel_index = sidebar.curselection()
    selection = all_items[sel_index[0]].strip()

def load_entry(_) -> None:
    update_selection(_)
    
    text_area.delete(1.0)

    # Remove the \n character to open correctly.
    with open(os.path.join(cons.DATA_FOLDER_PATH, selection)) as file:
        # Delete auto new line.
        text_area.replace(1.0, tk.END, file.read()[:-1])

def save_entry(_) -> None:
    global selection

    if selection is not None:
        with open(os.path.join(cons.DATA_FOLDER_PATH, selection), "w") as file:
            file.write(text_area.get(1.0, tk.END))

# Create the table.
root = tk.Tk()
# Maximize window.
root.state("zoomed")
root.resizable(False, False)
# Configure.
root.configure(bg="grey25")
root.title("MyJournal")

# Create sidebar.
sidebar = tk.Listbox(root, exportselection=False, bg="mistyrose4",fg="white", width=50)
sidebar.bind("<<ListboxSelect>>", func=save_entry, add="+")
sidebar.bind("<<ListboxSelect>>", func=load_entry, add="+")
sidebar.pack(side=tk.LEFT, fill=tk.BOTH)
sidebar.select_anchor(tk.END)
refresh()

# Top frame.
top_frame = tk.Frame(root, bg="grey25")
top_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=1)

# Top left.
topleft_frame = tk.Frame(top_frame, bg="grey25")
topleft_frame.pack(side=tk.LEFT, padx=50, pady=50)

add_entry_btn = tk.Button(topleft_frame, text="Add Entry",fg="white", width=10)
add_entry_btn.bind("<Button-1>", func=add_entry)
add_entry_btn.pack(side=tk.TOP, pady=10)
add_entry_btn.configure(bg="lightsteelblue3")

# Delete entry specifier.
del_entry: tk.Entry = tk.Entry(topleft_frame, bg="mistyrose4",fg="white")
del_entry.pack(side=tk.BOTTOM)

del_entry_btn = tk.Button(topleft_frame, text="Delete Entry",fg="white", width=10)
del_entry_btn.bind("<Button-1>", func=delete_entry)
del_entry_btn.pack(side=tk.BOTTOM, pady=10)
del_entry_btn.configure(bg="hotpink3")

# Top right.
topright_frame = tk.Frame(top_frame, bg="grey25")
topright_frame.pack(side=tk.RIGHT, padx=50, pady=50)

# Search bar.
search_label = tk.Label(topright_frame, text="Search phrase:",bg="grey25",fg="white", width=15)
search_label.pack(side=tk.TOP)

# Search prompt.
search_box = tk.Text(topright_frame, bg="mistyrose4",fg="white", height=1, width=20)
search_box.pack(side=tk.BOTTOM, pady=5)

# Create bottom frame.
bot_frame = tk.Frame(root, bg="grey25")
bot_frame.pack(side=tk.BOTTOM, padx=50, pady=50)
bot_frame.configure(bg="red")

# Text area.
text_area = tk.Text(bot_frame, bg="mistyrose4",fg="white")
text_area.pack()

root.mainloop()

if __name__ == "__main__":
    pass