# Generated by Django 3.0.7 on 2020-06-14 11:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20200614_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
