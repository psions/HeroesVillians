# Generated by Django 4.0.3 on 2022-03-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0006_remove_supertypes_hero_or_villain'),
    ]

    operations = [
        migrations.AddField(
            model_name='supertypes',
            name='side',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
