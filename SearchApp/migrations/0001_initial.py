# Generated by Django 4.2.1 on 2023-05-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=100)),
                ('std_Roll', models.CharField(max_length=10)),
                ('std_Dept', models.CharField(max_length=50)),
                ('std_city', models.CharField(max_length=50)),
            ],
        ),
    ]
