# Generated by Django 5.0.7 on 2024-07-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0004_alter_board_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="id",
            field=models.IntegerField(
                editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
