# Generated by Django 2.2.6 on 2019-11-15 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='schedule.User')),
                ('preference1', models.BooleanField(default=False)),
                ('preference2', models.BooleanField(default=False)),
                ('preference3', models.BooleanField(default=False)),
                ('preference1_prio', models.CharField(max_length=32)),
                ('preference2_prio', models.CharField(max_length=32)),
                ('preference3_prio', models.CharField(max_length=32)),
            ],
        ),
    ]
