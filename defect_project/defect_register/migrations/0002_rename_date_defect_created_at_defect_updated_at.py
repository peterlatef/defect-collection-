# Generated by Django 4.1.7 on 2023-04-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defect',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='defect',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
