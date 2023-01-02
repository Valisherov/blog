# Generated by Django 4.1.3 on 2022-12-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='year',
        ),
        migrations.AddField(
            model_name='education',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='year1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='year2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
