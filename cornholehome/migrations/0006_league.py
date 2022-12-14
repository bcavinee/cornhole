# Generated by Django 3.2.6 on 2022-08-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cornholehome', '0005_teams_total_win_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='league',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=200)),
                ('league_team_one', models.CharField(max_length=15)),
                ('league_team_one_record', models.CharField(default='0-0', max_length=20)),
                ('link_to_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cornholehome.teams')),
            ],
        ),
    ]
