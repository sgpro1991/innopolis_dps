# Generated by Django 2.1.3 on 2018-11-10 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_air', models.FloatField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('timezone', models.CharField(choices=[('0', 'MSK')], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='air',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Station'),
        ),
    ]
