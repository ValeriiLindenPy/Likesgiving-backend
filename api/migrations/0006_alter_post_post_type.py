# Generated by Django 4.2.4 on 2023-09-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_post_emotion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_type",
            field=models.CharField(
                choices=[("dislike", "Dislike"), ("like", "Like")], max_length=7
            ),
        ),
    ]
