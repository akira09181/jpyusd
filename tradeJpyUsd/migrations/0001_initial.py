# Generated by Django 3.1.6 on 2021-11-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.IntegerField(default=5, verbose_name='短い移動平均線')),
                ('long', models.IntegerField(default=14, verbose_name='長い移動平均線')),
                ('val', models.IntegerField(default=30, verbose_name='取引量')),
                ('start', models.IntegerField(default=1000000, verbose_name='初期投資額')),
            ],
        ),
    ]