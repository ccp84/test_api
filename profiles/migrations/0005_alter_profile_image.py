# Generated by Django 3.2.18 on 2023-04-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/'),
        ),
    ]
