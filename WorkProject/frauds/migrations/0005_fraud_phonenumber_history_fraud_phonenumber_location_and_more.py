# Generated by Django 4.2.7 on 2024-01-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frauds', '0004_alter_fraud_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='fraud',
            name='phonenumber_history',
            field=models.FileField(blank=True, null=True, upload_to='num_history/'),
        ),
        migrations.AddField(
            model_name='fraud',
            name='phonenumber_location',
            field=models.FileField(blank=True, null=True, upload_to='num_location/'),
        ),
        migrations.AlterField(
            model_name='fraud',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]