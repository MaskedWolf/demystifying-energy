# Generated by Django 3.0.5 on 2020-04-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default='saya', max_length=100),
            preserve_default=False,
        ),
    ]
