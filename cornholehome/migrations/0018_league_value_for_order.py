# Generated by Django 3.2.6 on 2022-09-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cornholehome', '0017_league_name_placeholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='value_for_order',
            field=models.IntegerField(default=99),
        ),
    ]