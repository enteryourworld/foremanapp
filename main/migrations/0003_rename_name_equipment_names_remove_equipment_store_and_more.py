# Generated by Django 4.2.9 on 2024-06-16 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_man_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='name',
            new_name='names',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='store',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='expirydate',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
    ]
