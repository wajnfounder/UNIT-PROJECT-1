from models.performance_record import PerformanceRecord


class PerformanceManager:

    def __init__(self, storage, kpi_manager):
        self.storage = storage
        self.kpi_manager = kpi_manager


    def record_progress(self, member_id, kpi_id, cycle_id, actual):

        # Get KPI to read target
        kpi = self.kpi_manager.get_kpi(kpi_id)

        if not kpi:
            raise ValueError("KPI not found")

        target = kpi.target

        # Calculate progress automatically
        progress = (actual / target) * 100

        record_id = self.storage.generate_id("performance_record")

        record = PerformanceRecord(
            record_id,
            member_id,
            kpi_id,
            cycle_id,
            round(progress, 2),
            actual
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


    def generate_report(self):

        records = self.storage.data["performance_records"]

        if not records:
            return None

        total_progress = 0
        top_record = None

        for record in records:

            total_progress += record["progress"]

            if top_record is None or record["progress"] > top_record["progress"]:
                top_record = record

        average_progress = total_progress / len(records)

        report = {
            "total_records": len(records),
            "average_progress": round(average_progress, 2),
            "top_member": top_record["member_id"],
            "top_progress": top_record["progress"]
        }

        return report