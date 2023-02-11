# Generated by Django 4.1.5 on 2023-02-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(blank=True, max_length=100, null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
