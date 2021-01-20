# Generated by Django 3.1.2 on 2021-01-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('element', models.CharField(max_length=20)),
                ('alloy', models.CharField(max_length=10)),
                ('shape', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]