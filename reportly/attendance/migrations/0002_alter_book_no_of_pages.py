# Generated by Django 3.2.8 on 2021-10-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='no_of_pages',
            field=models.IntegerField(default=10),
        ),
    ]
