from models.kpi import KPI


class KPIManager:

    def __init__(self, storage):
        self.storage = storage


    def create_kpi(self, name, weight, kpi_type, department_id):

        kpi_id = self.storage.generate_id("kpi")

        kpi = KPI(kpi_id, name, weight, kpi_type, department_id)

        self.storage.data["kpis"].append(kpi.to_dict())

        self.storage.save_data()

        return kpi


    def list_kpis(self):

        kpis = self.storage.data["kpis"]

        return [
            KPI.from_dict(kpi)
            for kpi in kpis
        ]


    def get_kpi(self, kpi_id):

        for kpi in self.storage.data["kpis"]:

            if kpi["id"] == kpi_id:
                return KPI.from_dict(kpi)

        return None