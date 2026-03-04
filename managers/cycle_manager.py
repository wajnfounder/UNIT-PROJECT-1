from models.evaluation_cycle import EvaluationCycle


class CycleManager:

    def __init__(self, storage):
        self.storage = storage


    def create_cycle(self, name):

        # التأكد أنه لا توجد دورة نشطة حالياً
        for cycle in self.storage.data["cycles"]:
            if cycle["status"] == "active":
                return None  # لا يسمح بوجود أكثر من دورة نشطة

        cycle_id = self.storage.generate_id("cycle")

        cycle = EvaluationCycle(cycle_id, name, "active")

        self.storage.data["cycles"].append(cycle.to_dict())

        self.storage.save_data()

        return cycle


    def list_cycles(self):

        return [
            EvaluationCycle.from_dict(cycle)
            for cycle in self.storage.data["cycles"]
        ]


    def close_cycle(self, cycle_id):

        for cycle in self.storage.data["cycles"]:
            if cycle["id"] == cycle_id:
                cycle["status"] = "closed"
                self.storage.save_data()
                return True

        return False


    def get_active_cycle(self):

        for cycle in self.storage.data["cycles"]:
            if cycle["status"] == "active":
                return EvaluationCycle.from_dict(cycle)

        return None