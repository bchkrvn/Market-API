# Generated by Django 3.2.6 on 2023-05-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/ads/'),
        ),
    ]
