from models.kpi import KPI


class KPIManager:

    # Initialize the manager with the storage system
    def __init__(self, storage):
        self.storage = storage

    # Create a new KPI and store it in the system
    def create_kpi(self, name, target, weight, kpi_type, department_id):
        kpi_id = self.storage.generate_id("kpi")

        kpi = KPI(kpi_id, name, target, weight, kpi_type, department_id)

        self.storage.data["kpis"].append(kpi.to_dict())

        self.storage.save_data()

        return kpi

    # Return all KPIs as KPI objects
    def list_kpis(self):
        kpis = self.storage.data["kpis"]

        return [
            KPI.from_dict(kpi)
            for kpi in kpis
        ]

    # Retrieve a specific KPI by its ID
    def get_kpi(self, kpi_id):
        for kpi in self.storage.data["kpis"]:
            if kpi["id"] == kpi_id:
                return KPI.from_dict(kpi)

        return None