# Generated by Django 5.0.3 on 2024-04-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_alter_chatsession_question_asked_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsession',
            name='retrieval_count',
            field=models.IntegerField(default=0),
        ),
    ]
