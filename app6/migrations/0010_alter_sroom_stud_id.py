# Generated by Django 4.2.1 on 2024-06-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0009_remove_student_room_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sroom',
            name='stud_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
