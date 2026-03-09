class TaskManager:

    def __init__(self, storage):
        self.storage = storage

    def add_task(self, member_id, kpi_id, description):

        task_id = self.storage.generate_id("task")

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
        return[
            task for task in self.storage.data["tasks"]
            if task["member_id"] == member_id
         
        ] 
    def complete_task(self, task_id):
        for task in self.storage.data["tasks"]:
            if task["id"] == task_id:
                task["status"] = "done"
                self.storage.save.data()
                return True
    
        return False
    