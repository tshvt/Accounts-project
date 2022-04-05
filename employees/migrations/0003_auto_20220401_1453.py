# Generated by Django 2.2 on 2022-04-01 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20220401_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parent_department',
            field=models.ForeignKey(default=models.CharField(max_length=100, unique=True), on_delete=django.db.models.deletion.CASCADE, to='employees.Department', to_field='name'),
        ),
    ]
