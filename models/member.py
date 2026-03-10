class Member:

    # Initialize a member with ID, name, role, and optional department
    def __init__(self, member_id: int, name: str, role: str, department_id=None):
        self.id = member_id
        self.name = name
        self.role = role
        self.department_id = department_id

    # Convert the member object into a dictionary for storage (JSON)
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "department_id": self.department_id
        }

    # Create a Member object from dictionary data
    @staticmethod
    def from_dict(data: dict):
        return Member(
            member_id=data["id"],
            name=data["name"],
            role=data["role"],
            department_id=data["department_id"]
        )