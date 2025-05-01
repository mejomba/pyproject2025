from django.db import models

from aaa.models.user_models import CustomUser


class AbstractCommModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    delete_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def jcreated_date(self):
        return 'jcreated_date'

    def jupdate_date(self):
        return 'jupdate_date'


class AbstractCommWithUserModel(AbstractCommModel):
    creator_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='%(app_label)s_creator_%(model_name)s')
    editor_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='%(app_label)s_editor_%(model_name)s')

    class Meta:
        abstract = True


class Category(AbstractCommWithUserModel):
    title = models.CharField(max_length=128)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='cats')
    is_menu = models.BooleanField(default=False)

