# Generated by Django 5.0.3 on 2024-04-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_remove_chatsession_cluster_chatsession_cluster_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='similarquestion',
            name='cluster_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
