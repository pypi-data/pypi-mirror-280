# Generated by Django 4.2.5 on 2024-01-24 04:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0003_conversation_session_key"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Conversation",
            new_name="ChatSession",
        ),
        migrations.RenameField(
            model_name="chatsession",
            old_name="session_key",
            new_name="user_id",
        ),
    ]
