# Generated by Django 4.2.5 on 2024-04-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0012_remove_trainclass_id_trainclass_class_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_journey',
            field=models.DateField(null=True),
        ),
    ]
