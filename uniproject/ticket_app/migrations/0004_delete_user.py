# Generated by Django 4.0.6 on 2022-08-16 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0003_alter_ticket_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
