# Generated by Django 4.0.4 on 2022-05-13 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assentamento_fucional', '0003_assentamentofuncional_status_afd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assentamentofuncional',
            old_name='Localizacao',
            new_name='localizacao',
        ),
    ]
