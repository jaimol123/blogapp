# Generated by Django 2.2.6 on 2019-10-30 10:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_slider_slider_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='step',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]