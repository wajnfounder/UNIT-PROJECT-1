import json
import os

class StorageManager:
    def __init__(self, file_path="data/data.json"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.file_path):
            return self._initialize_data_file()

        with open(self.file_path, "r") as file:
            return json.load(file)       
        

    def _initialize_data_file(self):
        initial_data = {
            "id_counters": {
                "department": 1,
                "member": 1,
                "kpi": 1,
                "cycle": 1,
                "performance_record": 1
            },
            "departments": [],
            "members": [],
            "kpis": [],
            "cycles": [],
            "performance_records": []
        }

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, "w") as file:
            json.dump(initial_data, file, indent=4)

        return initial_data
    

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)


    def generate_id(self, entity_name):
        current_id = self.data["id_counters"][entity_name]
        self.data["id_counters"][entity_name] += 1
        self.save_data()
        return current_id
    
        