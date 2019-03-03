# Generated by Django 2.1.7 on 2019-03-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0003_comment_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.TextField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='zipcode',
            field=models.TextField(max_length=5),
        ),
    ]
