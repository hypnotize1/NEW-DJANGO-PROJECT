# Generated by Django 5.0.2 on 2024-03-01 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
    ]
