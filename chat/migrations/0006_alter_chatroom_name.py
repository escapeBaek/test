# Generated by Django 5.0.7 on 2024-08-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0005_chatroom_alter_message_room_delete_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]