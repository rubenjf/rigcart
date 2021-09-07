# Generated by Django 3.1 on 2020-08-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='document',
            field=models.FileField(upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rig_choices',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('archieve', 'Archieve')], default='active', max_length=20, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rig_image',
            field=models.ImageField(default='images/anc-logo.png', upload_to='images'),
        ),
    ]