from models.member import Member


class MemberManager:

    def __init__(self, storage):
        self.storage = storage


    def create_member(self, name, role, department_id=None):

        member_id = self.storage.generate_id("member")

        member = Member(member_id, name, role, department_id)

        self.storage.data["members"].append(member.to_dict())

        self.storage.save_data()

        return member


    def list_members(self):

        members = self.storage.data["members"]

        return [
            Member.from_dict(member)
            for member in members
        ]


    def get_member(self, member_id):

        for member in self.storage.data["members"]:

            if member["id"] == member_id:
                return Member.from_dict(member)

        return None