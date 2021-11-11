# Generated by Django 3.2.6 on 2021-11-11 02:43

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='moodTypes',
            field=jsonfield.fields.JSONField(),
        ),
    ]
