# Generated by Django 2.2.6 on 2019-11-05 03:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0022_aboutus_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='image2',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='text1',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='feature',
            name='text1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='text2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]