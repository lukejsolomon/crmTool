# Generated by Django 3.2 on 2021-05-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210511_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bllAddrssSt',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='bllAddrssZp',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='shpAddrssSt',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='shpAddrssZp',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(choices=[('001', '001'), ('002', '002'), ('003', '003'), ('004', '004'), ('005', '005'), ('006', '006'), ('007', '007')], max_length=200, null=True),
        ),
    ]