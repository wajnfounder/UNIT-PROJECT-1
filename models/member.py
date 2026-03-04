class Member:
    def __init__(self, member_id: int, name: str, role: str, department_id=None):
        self.id = member_id
        self.name = name
        self.role = role
        self.department_id = department_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "department_id": self.department_id
        }

    @staticmethod
    def from_dict(data: dict):
        return Member(
            member_id=data["id"],
            name=data["name"],
            role=data["role"],
            department_id=data["department_id"]
        )