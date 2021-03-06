# Generated by Django 3.1.3 on 2020-11-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Nationality', models.CharField(max_length=30)),
                ('Freelance', models.CharField(default='Available', max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=30)),
                ('Facebook', models.CharField(max_length=30)),
                ('Langages', models.CharField(default='English', max_length=30)),
            ],
        ),
    ]
