# Generated by Django 2.2.6 on 2019-11-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_auto_20191031_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Slider'},
        ),
        migrations.AlterModelOptions(
            name='sociallinks',
            options={'verbose_name_plural': 'Social Links'},
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='social_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
