# Generated by Django 3.1.1 on 2020-09-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountainapp', '0002_auto_20200926_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='longtitude',
            field=models.FloatField(null=True),
        ),
    ]