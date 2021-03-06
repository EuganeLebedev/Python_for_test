# Generated by Django 3.0.5 on 2020-04-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200405_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ManyToManyField(to='blog.Topic'),
        ),
    ]
