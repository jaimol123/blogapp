# Generated by Django 2.2.6 on 2019-11-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0039_auto_20191112_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.EmailField(blank=True, max_length=25, null=True),
        ),
    ]