from models.evaluation_cycle import EvaluationCycle


class CycleManager:

    # Initialize the manager with the storage system
    def __init__(self, storage):
        self.storage = storage

    # Create a new evaluation cycle (only one active cycle allowed)
    def create_cycle(self, name):

        for cycle in self.storage.data["cycles"]:
            if cycle["status"] == "active":
                return None

        cycle_id = self.storage.generate_id("cycle")

        cycle = EvaluationCycle(cycle_id, name, "active")

        self.storage.data["cycles"].append(cycle.to_dict())

        self.storage.save_data()

        return cycle

    # Return all cycles as EvaluationCycle objects
    def list_cycles(self):

        cycles = self.storage.data["cycles"]

        return [EvaluationCycle.from_dict(cycle) for cycle in cycles]

    # Close an active cycle
    def close_cycle(self, cycle_id):

        for cycle in self.storage.data["cycles"]:
            if cycle["id"] == cycle_id:
                cycle["status"] = "closed"
                self.storage.save_data()
                return True

        return False

    # Retrieve the currently active cycle
    def get_active_cycle(self):

        for cycle in self.storage.data["cycles"]:
            if cycle["status"] == "active":
                return EvaluationCycle.from_dict(cycle)

        return None