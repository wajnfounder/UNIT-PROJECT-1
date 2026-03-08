class KPI:
    def __init__(self, kpi_id: int, name: str, target: float, weight: int, kpi_type: str, department_id: int):
        self.id = kpi_id
        self.name = name
        self.target = target
        self.weight = weight
        self.type = kpi_type
        self.department_id = department_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "target": self.target,
            "weight": self.weight,
            "type": self.type,
            "department_id": self.department_id
        }

    @staticmethod
    def from_dict(data: dict):
        return KPI(
            kpi_id=data["id"],
            name=data["name"],
            target=data["target"],
            weight=data["weight"],
            kpi_type=data["type"],
            department_id=data["department_id"]
        )
    