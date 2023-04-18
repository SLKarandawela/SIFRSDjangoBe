# Generated by Django 4.2 on 2023-04-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=512)),
                ('user_image', models.FileField(upload_to='')),
                ('dob', models.DateTimeField()),
                ('skin_type', models.IntegerField()),
                ('gender', models.CharField(default='M', max_length=10)),
                ('uk_size', models.CharField(default='XL', max_length=10)),
            ],
        ),
    ]
