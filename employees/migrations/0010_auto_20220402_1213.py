# Generated by Django 2.2 on 2022-04-02 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20220402_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parent_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Department', to_field='name'),
        ),
    ]
