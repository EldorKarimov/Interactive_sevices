# Generated by Django 4.2 on 2023-05-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='media/users/user_picture.png', upload_to='media/users'),
        ),
    ]