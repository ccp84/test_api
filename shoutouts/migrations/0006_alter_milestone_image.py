# Generated by Django 3.2.18 on 2023-04-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoutouts', '0005_alter_milestone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
        ),
    ]
