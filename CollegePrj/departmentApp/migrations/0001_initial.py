# Generated by Django 3.2.7 on 2021-09-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=30)),
                ('dep_year_of_establishment', models.IntegerField()),
                ('dep_course_duration', models.IntegerField()),
            ],
        ),
    ]
