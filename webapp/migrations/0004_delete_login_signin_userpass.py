# Generated by Django 5.0.7 on 2024-11-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='signin',
            name='userPass',
            field=models.JSONField(default={'': ''}, max_length=200),
        ),
    ]
