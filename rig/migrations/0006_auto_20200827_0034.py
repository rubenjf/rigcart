# Generated by Django 3.1 on 2020-08-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rig', '0005_event_current_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='rig_choices',
            field=models.CharField(choices=[('Active', 'Active'), ('Archieve', 'Archieve')], default='Active', max_length=20, verbose_name='rig Type'),
        ),
    ]