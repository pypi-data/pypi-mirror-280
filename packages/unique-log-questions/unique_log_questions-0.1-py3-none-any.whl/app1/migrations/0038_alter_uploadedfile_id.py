# Generated by Django 5.0.3 on 2024-04-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_alter_similarquestion_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
