# Generated by Django 3.0.7 on 2020-06-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksys', '0007_auto_20200627_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveacc',
            name='currency',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='saveacc',
            name='interest_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
