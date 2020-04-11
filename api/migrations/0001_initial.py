# Generated by Django 3.0.5 on 2020-04-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('count', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
