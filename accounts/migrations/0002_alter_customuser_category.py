# Generated by Django 5.2.1 on 2025-06-14 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="category",
            field=models.CharField(
                choices=[("student", "Student"), ("teacher", "Teacher")], max_length=20
            ),
        ),
    ]
