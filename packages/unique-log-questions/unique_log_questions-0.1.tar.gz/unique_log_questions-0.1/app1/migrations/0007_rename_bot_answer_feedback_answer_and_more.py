# Generated by Django 5.0.3 on 2024-03-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='bot_answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='is_helpful',
            new_name='feedback',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='question_id',
        ),
        migrations.AddField(
            model_name='feedback',
            name='question',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
