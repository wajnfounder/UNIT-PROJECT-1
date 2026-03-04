class EvaluationCycle:
    def __init__(self, cycle_id: int, name: str, status: str):
        self.id = cycle_id
        self.name = name
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        return EvaluationCycle(
            cycle_id=data["id"],
            name=data["name"],
            status=data["status"]
        )