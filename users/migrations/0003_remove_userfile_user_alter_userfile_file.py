# Generated by Django 4.1.5 on 2023-12-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_person_userfile_delete_loginform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='user',
        ),
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
