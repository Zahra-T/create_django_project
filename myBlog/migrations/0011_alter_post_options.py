# Generated by Django 3.2.15 on 2022-09-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0010_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_at']},
        ),
    ]
