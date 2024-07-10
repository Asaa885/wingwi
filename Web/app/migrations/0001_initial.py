# Generated by Django 5.0.6 on 2024-07-09 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combName', models.CharField(max_length=100)),
                ('combCode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=100)),
                ('Combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.combination')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('date_reported', models.DateField(auto_now_add=True)),
                ('address', models.TextField()),
                ('nida_id', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(default='active', max_length=10)),
                ('combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.combination')),
            ],
        ),
    ]