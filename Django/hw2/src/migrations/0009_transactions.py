# Generated by Django 3.2.7 on 2021-10-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_auto_20211006_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
