# Generated by Django 2.2 on 2019-05-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projektwahl', '0003_auto_20190505_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='schueler',
            name='klasse',
            field=models.CharField(default='Q1', max_length=3),
            preserve_default=False,
        ),
    ]
