# Generated by Django 4.2.2 on 2023-07-06 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-created_at']},
        ),
    ]
