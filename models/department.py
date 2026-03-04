class Department:
    def __init__(self, department_id: int, name: str):
        self.id = department_id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def from_dict(data: dict):
        return Department(
            department_id=data["id"],
            name=data["name"]
        )
    
    