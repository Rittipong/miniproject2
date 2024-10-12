# Generated by Django 5.1 on 2024-10-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_data_person_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='blackmyt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cyberpunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='minecrafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='spiderman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]
