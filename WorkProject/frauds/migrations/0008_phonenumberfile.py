# Generated by Django 4.2.7 on 2024-01-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frauds', '0007_alter_imei_date_to_alter_imei_date_up_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhonenumberFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='num_location/')),
            ],
        ),
    ]