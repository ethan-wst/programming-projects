# Generated by Django 5.0.3 on 2024-03-19 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_class_assignment_weights_assignment_grades_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='assignment_grades',
            old_name='class_number',
            new_name='course_number',
        ),
        migrations.RenameField(
            model_name='assignment_weights',
            old_name='class_number',
            new_name='course_number',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_grade',
            new_name='course_grade',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_name',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_number',
            new_name='course_number',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_term',
            new_name='course_term',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_year',
            new_name='course_year',
        ),
    ]
