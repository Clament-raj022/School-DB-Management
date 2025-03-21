# Generated by Django 5.0.3 on 2024-08-22 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Member', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), ('Admin', 'Admin')], max_length=50)),
            ],
            options={
                'db_table': 'Login Form',
            },
        ),
        migrations.CreateModel(
            name='registration_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=50, null=True)),
                ('mail', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(choices=[('India', 'India'), ('USA', 'America'), ('other', 'Other')], max_length=50)),
                ('profile', models.FileField(null=True, upload_to='')),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('status', models.IntegerField(default=1, editable=False)),
            ],
            options={
                'db_table': 'teacher_registration',
            },
        ),
        migrations.CreateModel(
            name='stud_registration_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('Clas', models.CharField(choices=[('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th')], max_length=50)),
                ('date_of_birth', models.DateField(default=datetime.date.today, null=True)),
                ('mail', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('your_reister_no_is', models.CharField(max_length=10, null=True)),
                ('profile', models.FileField(null=True, upload_to='')),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('status', models.IntegerField(default=1, editable=False)),
            ],
            options={
                'db_table': 'student_registration',
            },
        ),
        migrations.CreateModel(
            name='student_marks_register_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stu_id', models.IntegerField(null=True)),
                ('tamil', models.IntegerField(null=True)),
                ('english', models.IntegerField(null=True)),
                ('maths', models.IntegerField(null=True)),
                ('science', models.IntegerField(null=True)),
                ('social', models.IntegerField(null=True)),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('status', models.IntegerField(default=1, editable=False)),
            ],
            options={
                'db_table': 'student_marks_register',
            },
        ),
    ]
