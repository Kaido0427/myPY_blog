# Generated by Django 4.2.2 on 2023-11-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]