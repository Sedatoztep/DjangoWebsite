# Generated by Django 3.2.9 on 2023-06-10 12:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
