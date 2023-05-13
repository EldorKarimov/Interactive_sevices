# Generated by Django 4.2 on 2023-05-09 06:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=128, unique=True)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SendData',
            fields=[
                ('num', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('faculty', models.CharField(choices=[('TTKT', 'Telekomunikatsiya texnologiyalari va kasb talimi')], default='TTKT', max_length=5)),
                ('direction', models.CharField(choices=[('AX', 'Axborot xavfsizligi'), ('DI', 'Dasturiy injinering')], default='AX', max_length=5)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('upload', models.FileField(upload_to='uploads')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactive.leader')),
            ],
        ),
    ]
