# Generated by Django 4.0.3 on 2022-04-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
