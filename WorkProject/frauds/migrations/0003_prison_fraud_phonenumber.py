# Generated by Django 4.2.7 on 2024-01-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frauds', '0002_alter_fraud_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('lat', models.CharField(max_length=220)),
                ('lon', models.CharField(max_length=220)),
                ('address', models.CharField(max_length=220)),
                ('oblast', models.CharField(max_length=220)),
            ],
        ),
        migrations.AddField(
            model_name='fraud',
            name='phonenumber',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
