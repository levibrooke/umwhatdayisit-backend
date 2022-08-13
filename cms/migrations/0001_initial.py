# Generated by Django 4.1 on 2022-08-09 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfWeek', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=512)),
                ('mediaType', models.CharField(choices=[('image', 'image'), ('video', 'video'), ('twitter-embed', 'twitter-embed')], max_length=512)),
                ('mediaLink', models.URLField()),
                ('alt', models.CharField(max_length=512)),
                ('message', models.TextField()),
            ],
        ),
    ]