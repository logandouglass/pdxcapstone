# Generated by Django 4.0.4 on 2022-06-01 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0003_composition_chord1_quality_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='composition',
            old_name='chord1',
            new_name='chord1_tonic',
        ),
        migrations.RenameField(
            model_name='composition',
            old_name='chord2',
            new_name='chord2_tonic',
        ),
        migrations.RenameField(
            model_name='composition',
            old_name='chord3',
            new_name='chord3_tonic',
        ),
        migrations.RenameField(
            model_name='composition',
            old_name='chord4',
            new_name='chord4_tonic',
        ),
        migrations.RenameField(
            model_name='composition',
            old_name='chord5',
            new_name='chord5_tonic',
        ),
    ]