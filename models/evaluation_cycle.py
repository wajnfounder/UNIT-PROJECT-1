class EvaluationCycle:

    # Initialize an evaluation cycle with its ID, name, and status
    def __init__(self, cycle_id: int, name: str, status: str):
        self.id = cycle_id
        self.name = name
        self.status = status

    # Convert the evaluation cycle object into a dictionary for storage (JSON)
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status
        }

    # Create an EvaluationCycle object from dictionary data
    @staticmethod
    def from_dict(data: dict):
        return EvaluationCycle(
            cycle_id=data["id"],
            name=data["name"],
            status=data["status"]
        )