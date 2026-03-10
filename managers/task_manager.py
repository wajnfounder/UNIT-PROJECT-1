class TaskManager:

    def __init__(self, storage):
        self.storage = storage


    def add_task(self, member_id, kpi_id, description):

        task_id = self.storage.generate_id("tasks")

        task = {
            "id": task_id,
            "member_id": member_id,
            "kpi_id": kpi_id,
            "description": description,
            "status": "pending"
        }

        self.storage.data["tasks"].append(task)

        self.storage.save_data()

        return task


    def list_tasks(self):
        return self.storage.data["tasks"]


    def get_number_tasks(self, member_id):

        return [
            task for task in self.storage.data["tasks"]
            if task["member_id"] == member_id
        ]


    def complete_task(self, task_id):

        for task in self.storage.data["tasks"]:

            if task["id"] == task_id:

                task["status"] = "completed"

                self.storage.save_data()

                # calculate progress for the member within the KPI
                member_tasks = [
                    t for t in self.storage.data["tasks"]
                    if t["member_id"] == task["member_id"]
                    and t["kpi_id"] == task["kpi_id"]
                ]

                total = len(member_tasks)

                if total == 0:
                    return 0

                completed = len([
                    t for t in member_tasks
                    if t["status"] == "completed"
                ])

                progress = (completed / total) * 100

                return round(progress, 2)

        return None


    def pending_task(self, task_id):

        for task in self.storage.data["tasks"]:

            if task["id"] == task_id:

                task["status"] = "pending"

                self.storage.save_data()

                return True

        return False