# Generated by Django 5.0.7 on 2024-12-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_rename_disc_contact_cdisc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='conf',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='userPass',
            field=models.JSONField(max_length=200, null=True),
        ),
    ]
