class PerformanceRecord:
    def __init__(self, record_id: int, member_id: int, kpi_id: int, cycle_id: int, progress: int, calculated_score: float = 0):
        self.id = record_id
        self.member_id = member_id
        self.kpi_id = kpi_id
        self.cycle_id = cycle_id
        self.progress = progress
        self.calculated_score = calculated_score

    def to_dict(self):
        return {
            "id": self.id,
            "member_id": self.member_id,
            "kpi_id": self.kpi_id,
            "cycle_id": self.cycle_id,
            "progress": self.progress,
            "calculated_score": self.calculated_score
        }

    @staticmethod
    def from_dict(data: dict):
        return PerformanceRecord(
            record_id=data["id"],
            member_id=data["member_id"],
            kpi_id=data["kpi_id"],
            cycle_id=data["cycle_id"],
            progress=data["progress"],
            calculated_score=data["calculated_score"]
        )