# Generated by Django 4.0.3 on 2022-03-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0004_remove_supertypes_hero_remove_supertypes_villain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supertypes',
            name='hero_or_villain',
            field=models.CharField(choices=[('Hero', 'Hero'), ('Villain', 'Villain')], default='Hero', max_length=255),
        ),
    ]
