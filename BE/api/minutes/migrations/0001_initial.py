# Generated by Django 4.0.3 on 2022-04-03 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=300)),
                ('conclusion', models.TextField(blank=True, max_length=300)),
                ('is_closed', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_assignee', models.BooleanField(default=False)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.member')),
                ('minute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutes.minute')),
            ],
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, max_length=2000)),
                ('summary', models.TextField(blank=True, max_length=400)),
                ('cloud_keyword', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('record_file', models.FileField(blank=True, null=True, upload_to='record/')),
                ('minute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutes.minute')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='minutes.participant')),
            ],
        ),
        migrations.CreateModel(
            name='SpeechFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_file', models.FileField(blank=True, null=True, upload_to='speech/')),
                ('speech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutes.speech')),
            ],
        ),
        migrations.CreateModel(
            name='SpeechComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.member')),
                ('speech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutes.speech')),
            ],
        ),
        migrations.CreateModel(
            name='MinuteFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_file', models.FileField(blank=True, null=True, upload_to='minute/')),
                ('minute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutes.minute')),
            ],
        ),
    ]
