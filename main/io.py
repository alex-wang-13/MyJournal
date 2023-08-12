import os
import datetime as date

import constants as con

def make_entry(title: str) -> None:
    """
    Creates an entry to the journal.

    Parameters:
        title (str): A title for the journal entry.

    Raises:
        RuntimeError: If the title is not provided, invalid, or
            already-existing.
    """

    if title is None:
        raise RuntimeError("Title cannot be empty.")
    
    title = "".join([c for c in title if c.isalnum() or c in ['.', '-', '_']])

    if not title:
        raise RuntimeError("Filtered title cannot be empty.")

    if os.path.exists(os.path.join(con.DATA_FOLDER_PATH, title)):
        raise RuntimeError("Entry already exists.")

    with open(os.path.join(con.DATA_FOLDER_PATH, title), "w") as file:
        file.write(date.date.today().strftime(format="%d/%m/%Y, %H:%M:%S"))