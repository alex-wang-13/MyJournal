import constants as cons

import os

class DB:
    def __init__(self) -> None:
        """
        A constructor for this BD.

        Gets the entries for this DB from a file.
        """
        
        self.entries: dict[int, str] = dict()
        
        # Initialize entries.
        with open(cons.USR_CNSTS_PATH) as file:
            for id, line in enumerate(file):
                self.entries[id] = line.strip()

    def get_entry(self, id: int) -> str:
        return self.entries.get(id)

    def add_entry(self, id: int, path: str) -> None:
        if self.get_entry(id) is None:
            self.entries[id] = path

            with open(cons.USR_CNSTS_PATH, "a") as file:
                file.writelines("".join([path, "\n"]))

            # Create file.
            with open(os.path.join(cons.DATA_FOLDER_PATH, path), mode="x") as file:
                pass

    def remove_entry(self, entry: str) -> str:
        if entry in self.entries.values():
            with open(cons.USR_CNSTS_PATH, "r") as file:
                lines: list[str] = file.readlines()

            # Remove the requested file.
            filtered_lines: list[str] = []
            for line in lines:
                if entry not in line:
                    filtered_lines.append(line)
                else:
                    os.remove(os.path.join(cons.DATA_FOLDER_PATH, line[:-1]))
                    self.entries = {key: value for key, value in self.entries.items() if value != line[:-1]}

            with open(cons.USR_CNSTS_PATH, "w") as file:
                file.writelines(filtered_lines)