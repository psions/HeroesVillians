# Generated by Django 4.0.3 on 2022-03-21 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0007_supertypes_side'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supertypes',
            name='side',
        ),
    ]
