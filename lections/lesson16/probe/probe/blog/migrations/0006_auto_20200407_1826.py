# Generated by Django 3.0.5 on 2020-04-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
