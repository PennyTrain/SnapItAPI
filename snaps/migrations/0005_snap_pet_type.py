# Generated by Django 3.2.25 on 2024-05-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0004_auto_20240520_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='snap',
            name='pet_type',
            field=models.CharField(default='Other', max_length=100),
        ),
    ]