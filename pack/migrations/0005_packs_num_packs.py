# Generated by Django 3.2.4 on 2021-06-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0004_remove_packs_num_packs'),
    ]

    operations = [
        migrations.AddField(
            model_name='packs',
            name='num_packs',
            field=models.SmallIntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
