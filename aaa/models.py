from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(verbose_name='تلفن همراه', max_length=11, unique=True, null=True, blank=True,
                             validators=[RegexValidator(r'^09\d{9}',
                                                        message='تلفن نا معتبر',
                                                        code='invalid_phone')])
    update_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    delete_date = models.DateTimeField(null=True, blank=True)
    is_special = models.BooleanField(default=False)
    creator_user = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='creators')
    editor_user = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='editors')

    USERNAME_FIELD = 'phone'
