# Generated by Django 4.1.2 on 2023-12-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_about_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]