# Generated by Django 3.0.5 on 2020-04-07 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200405_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='e_lebedev', on_delete=django.db.models.deletion.CASCADE, to='blog.Author'),
            preserve_default=False,
        ),
    ]
