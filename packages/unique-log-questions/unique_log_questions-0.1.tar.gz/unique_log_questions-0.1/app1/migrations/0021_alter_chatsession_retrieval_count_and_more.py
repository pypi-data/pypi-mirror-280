# Generated by Django 5.0.3 on 2024-04-03 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_chatsession_retrieval_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatsession',
            name='retrieval_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='chatsession',
            name='session_id',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='chatsession',
            name='user_identifier',
            field=models.CharField(max_length=4),
        ),
    ]
