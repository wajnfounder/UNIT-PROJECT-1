from models.performance_record import PerformanceRecord


class PerformanceManager:

    def __init__(self, storage):
        self.storage = storage


    def record_progress(self, member_id, kpi_id, cycle_id, progress):

        record_id = self.storage.generate_id("performance_record")

        record = PerformanceRecord(
            record_id,
            member_id,
            kpi_id,
            cycle_id,
            progress,
            0
        )

        self.storage.data["performance_records"].append(record.to_dict())

        self.storage.save_data()

        return record


    def list_records(self):

        records = self.storage.data["performance_records"]

        return [
            PerformanceRecord.from_dict(record)
            for record in records
        ]


    def get_member_records(self, member_id):

        return [
            PerformanceRecord.from_dict(record)
            for record in self.storage.data["performance_records"]
            if record["member_id"] == member_id
        ]