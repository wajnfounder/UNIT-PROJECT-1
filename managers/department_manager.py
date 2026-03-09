from models.department import Department


class DepartmentManager:

    # Initialize the manager with the storage system
    def __init__(self, storage):
        self.storage = storage

    # Create a new department and store it in the system
    def create_department(self, name):
        department_id = self.storage.generate_id("department")

        department = Department(department_id, name)

        self.storage.data["departments"].append(department.to_dict())

        self.storage.save_data()

        return department

    # Return all departments as Department objects
    def list_departments(self):
        departments = self.storage.data["departments"]

        return [
            Department.from_dict(dept)
            for dept in departments
        ]

    # Retrieve a specific department by its ID
    def get_department(self, department_id):
        for dept in self.storage.data["departments"]:
            if dept["id"] == department_id:
                return Department.from_dict(dept)

        return None