# Generated by Django 4.0.6 on 2022-07-28 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='date_of_field',
            new_name='date',
        ),
    ]