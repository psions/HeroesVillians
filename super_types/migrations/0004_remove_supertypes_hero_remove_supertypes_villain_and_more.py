# Generated by Django 4.0.3 on 2022-03-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0003_alter_supertypes_hero_alter_supertypes_villain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supertypes',
            name='hero',
        ),
        migrations.RemoveField(
            model_name='supertypes',
            name='villain',
        ),
        migrations.AddField(
            model_name='supertypes',
            name='hero_or_villain',
            field=models.CharField(choices=[('H', 'Hero'), ('V', 'Villain')], default='Hero', max_length=255),
        ),
    ]
