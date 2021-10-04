# Generated by Django 3.2.7 on 2021-10-04 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_test_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('age', models.SmallIntegerField(default=0)),
                ('phone', models.SmallIntegerField(blank=True, db_index=True, default=0)),
                ('info', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]