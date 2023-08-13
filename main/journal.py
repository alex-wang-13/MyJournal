import tkinter as tk
import db

# Initialize database.
data = db.DB()

def refresh() -> None:
    sidebar.delete(0, tk.END)

    for path in data.entries.values():
        sidebar.insert(tk.END, path)

def add_entry(_) -> None:
    data.add_entry(len(data.entries), path="".join(["test", str(len(data.entries))]))
    refresh()

def delete_entry(_) -> None:
    data.remove_entry(len(data.entries)-1)
    refresh()

# Create the table.
root = tk.Tk()
# Maximize window.
root.state("zoomed")
root.resizable(False, False)
# Configure.
root.configure(bg="lightgrey")
root.title("MyJournal")

# Create sidebar.
sidebar = tk.Listbox(root)
sidebar.pack(side=tk.LEFT, fill=tk.BOTH)
refresh()

# Top frame.
top_frame = tk.Frame(root, bg="lightgrey")
top_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=1)

# Top left.
topleft_frame = tk.Frame(top_frame, bg="lightgrey")
topleft_frame.pack(side=tk.LEFT, padx=50, pady=50)

add_entry_btn = tk.Button(topleft_frame, text="Add Entry", width=10)
add_entry_btn.bind("<Button-1>", func=add_entry)
add_entry_btn.pack(side=tk.TOP, pady=10)
add_entry_btn.configure(bg="lightblue")

del_entry_btn = tk.Button(topleft_frame, text="Delete Entry", width=10)
del_entry_btn.bind("<Button-1>", func=delete_entry)
del_entry_btn.pack(side=tk.BOTTOM, pady=10)
del_entry_btn.configure(bg="lightpink")

# Top right.
topright_frame = tk.Frame(top_frame, bg="lightgrey")
topright_frame.pack(side=tk.RIGHT, padx=50, pady=50)

# Search bar.
search_label = tk.Label(topright_frame, text="Search phrase:",bg="lightgrey", width=15)
search_label.pack(side=tk.TOP)

# Search prompt.
search_box = tk.Text(topright_frame, height=1, width=20)
search_box.pack(side=tk.BOTTOM, pady=5)

# Create bottom frame.
bot_frame = tk.Frame(root, bg="lightgrey")
bot_frame.pack(side=tk.BOTTOM, padx=50, pady=50)
bot_frame.configure(bg="red")

text_area = tk.Text(bot_frame)
text_area.pack()

root.mainloop()

if __name__ == "__main__":
    pass