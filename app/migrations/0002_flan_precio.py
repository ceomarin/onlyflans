# Generated by Django 3.2.4 on 2022-05-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='precio',
            field=models.IntegerField(default=0, max_length=200000),
            preserve_default=False,
        ),
    ]
