# Generated by Django 5.0.1 on 2024-01-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_user_first_name_remove_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics/'),
        ),
    ]
