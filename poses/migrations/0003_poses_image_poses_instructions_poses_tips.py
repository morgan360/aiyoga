# Generated by Django 4.1.5 on 2023-02-17 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_alter_yogaimage_image'),
        ('poses', '0002_rename_english_name_poses_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poses',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='display.yogaimage'),
        ),
        migrations.AddField(
            model_name='poses',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poses',
            name='tips',
            field=models.TextField(blank=True, null=True),
        ),
    ]
