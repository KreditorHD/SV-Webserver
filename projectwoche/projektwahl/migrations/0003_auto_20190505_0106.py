# Generated by Django 2.2 on 2019-05-05 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projektwahl', '0002_projekt_mitglieder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projekt',
            old_name='grösse',
            new_name='groesse',
        ),
    ]
