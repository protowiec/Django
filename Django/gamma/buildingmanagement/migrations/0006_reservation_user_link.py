# Generated by Django 4.0.3 on 2022-05-22 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buildingmanagement', '0005_room_max_people_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
