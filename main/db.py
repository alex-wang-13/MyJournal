import constants as cons

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
                self.entries[id] = line

    def get_entry(self, id: int) -> str:
        return self.entries.get(id)

    #TODO add entry ids automatically.
    def add_entry(self, id: int, path: str) -> None:
        if self.get_entry(id) is None:
            self.entries[id] = path

            with open(cons.USR_CNSTS_PATH, "a") as file:
                file.writelines("".join([path, "\n"]))

    def remove_entry(self, id: int) -> str:
        if self.get_entry(id) is not None:
            word: str = self.entries.pop(id)

            with open(cons.USR_CNSTS_PATH, "r") as file:
                lines: list[str] = file.readlines()

            filtered_lines: list[str] = [line for line in lines if word not in line]

            with open(cons.USR_CNSTS_PATH, "w") as file:
                file.writelines(filtered_lines)