# Generated by Django 3.0.14 on 2024-02-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales_data1',
            old_name='Gender',
            new_name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='sales_data1',
            name='mobile_no',
        ),
        migrations.AddField(
            model_name='sales_data1',
            name='password',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
