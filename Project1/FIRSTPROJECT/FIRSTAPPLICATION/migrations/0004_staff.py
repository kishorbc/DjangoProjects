# Generated by Django 3.1.7 on 2021-03-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Name', models.CharField(max_length=25)),
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]
