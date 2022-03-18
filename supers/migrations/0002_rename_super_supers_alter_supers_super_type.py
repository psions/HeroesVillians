# Generated by Django 4.0.3 on 2022-03-18 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='super',
            new_name='Supers',
        ),
        migrations.AlterField(
            model_name='supers',
            name='super_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super_types.supertypes'),
        ),
    ]
