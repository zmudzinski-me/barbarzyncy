from group.models import Group


class GroupRepository:
    @staticmethod
    def get_groups():
        return Group.objects.all()
