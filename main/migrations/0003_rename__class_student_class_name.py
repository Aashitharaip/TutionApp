# Generated by Django 5.1.2 on 2024-12-21 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_fees_fee_alter_class_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='_class',
            new_name='class_name',
        ),
    ]
