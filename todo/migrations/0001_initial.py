# Generated by Django 4.0.3 on 2022-05-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('detail', models.TextField()),
                ('indicator', models.CharField(choices=[('Urgent', 'Urgently '), ('Normal', 'Normal'), ('Low', 'Lower')], max_length=10)),
            ],
        ),
    ]
