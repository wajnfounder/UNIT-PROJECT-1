import json
import os


class StorageManager:

    # Initialize the storage manager and load existing data
    def __init__(self, file_path: str = "data/data.json"):
        self.file_path = file_path
        self.data = self._load_data()

    # Load data from the JSON file, or create it if it doesn't exist
    def _load_data(self) -> dict:

        if not os.path.exists(self.file_path):
            return self._initialize_data_file()

        try:
            with open(self.file_path, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            # Recreate file if corrupted
            return self._initialize_data_file()

    # Create the initial data structure and JSON file
    def _initialize_data_file(self) -> dict:

        initial_data = {
            "id_counters": {
                "department": 1,
                "member": 1,
                "kpi": 1,
                "cycle": 1,
                "performance_record": 1,
                "tasks": 1
            },
            "departments": [],
            "members": [],
            "kpis": [],
            "cycles": [],
            "performance_records": [],
            "tasks": []
        }

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, "w") as file:
            json.dump(initial_data, file, indent=4)

        return initial_data

    # Save the current in-memory data back to the JSON file
    def save_data(self):

        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    # Generate a new unique ID for a given entity type
    def generate_id(self, entity_name: str) -> int:

        current_id = self.data["id_counters"][entity_name]
        self.data["id_counters"][entity_name] += 1

        self.save_data()

        return current_id