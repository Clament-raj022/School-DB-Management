# Generated by Django 5.0.3 on 2024-08-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_marks_register_model',
            name='percentage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_marks_register_model',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
