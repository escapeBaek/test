# Generated by Django 5.0.7 on 2024-08-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0006_alter_chatroom_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]