from models.member import Member


class MemberManager:

    # Initialize the manager with the storage system
    def __init__(self, storage):
        self.storage = storage

    # Create a new member and store it in the system
    def create_member(self, name, role, department_id=None):

        member_id = self.storage.generate_id("member")

        member = Member(member_id, name, role, department_id)

        self.storage.data["members"].append(member.to_dict())

        self.storage.save_data()

        return member

    # Return all members as Member objects
    def list_members(self):

        members = self.storage.data["members"]

        return [Member.from_dict(member) for member in members]

    # Retrieve a specific member by ID
    def get_member(self, member_id):

        for member in self.storage.data["members"]:
            if member["id"] == member_id:
                return Member.from_dict(member)

        return None
    