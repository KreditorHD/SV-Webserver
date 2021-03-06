# Generated by Django 2.2 on 2019-04-19 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lehrer', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('grösse', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schueler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('projekt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projektwahl.Projekt')),
            ],
        ),
    ]
