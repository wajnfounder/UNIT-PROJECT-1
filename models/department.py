class Department:

    # Initialize a department object with its basic information
    def __init__(self, department_id: int, name: str):
        self.id = department_id
        self.name = name

    # Convert the department object into a dictionary for JSON storage
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }

    # Create a Department object from stored dictionary data
    @staticmethod
    def from_dict(data: dict):
        return Department(
            department_id=data["id"],
            name=data["name"]
        )