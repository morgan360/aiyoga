from import_export import resources, fields
from .models import CustomUser
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.contrib.auth.models import Group


class UserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'description',  'first_name', 'last_name')

    #
    # def after_save_instance(self, instance, using_transactions, dry_run):
    #     user = CustomUser.objects.get(username=instance.username)
    #     g = Group.objects.get(name="guardian")
    #     g.user_set.add(user)
    #     user.save()
