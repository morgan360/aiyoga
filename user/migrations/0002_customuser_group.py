# Generated by Django 4.1.5 on 2023-02-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.CharField(choices=[('novice', 'Novice'), ('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='regular', max_length=100),
        ),
    ]