# Generated by Django 5.1.5 on 2025-07-11 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_creator_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_date',
            new_name='updated_at',
        ),
    ]
