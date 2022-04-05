# Generated by Django 2.2 on 2022-04-01 14:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('rights_num', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1023), django.core.validators.MinValueValidator(0)])),
                ('parent_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Department', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('timezone', models.CharField(max_length=20)),
                ('rights_num', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1023), django.core.validators.MinValueValidator(0)])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Department')),
            ],
        ),
    ]
