# Generated by Django 2.0a1 on 2017-10-10 17:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171010_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='random_int',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]