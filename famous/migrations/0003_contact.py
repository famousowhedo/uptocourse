# Generated by Django 3.1.3 on 2020-11-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(default='your name', max_length=30)),
                ('you_email', models.EmailField(default='your email', max_length=254)),
                ('your_message', models.TextField(default='your message')),
            ],
        ),
    ]
