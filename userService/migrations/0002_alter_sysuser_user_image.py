# Generated by Django 4.2 on 2023-04-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysuser',
            name='user_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]