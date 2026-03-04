from models.department import Department


class DepartmentManager:

    def __init__(self, storage):
        self.storage = storage


    def create_department(self, name):

        department_id = self.storage.generate_id("department")

        department = Department(department_id, name)

        self.storage.data["departments"].append(department.to_dict())

        self.storage.save_data()

        return department


    def list_departments(self):

        departments = self.storage.data["departments"]

        return [
            Department.from_dict(dept)
            for dept in departments
        ]


    def get_department(self, department_id):

        for dept in self.storage.data["departments"]:

            if dept["id"] == department_id:
                return Department.from_dict(dept)

        return None