# Generated by Django 4.2.7 on 2023-11-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='id чата'),
        ),
    ]