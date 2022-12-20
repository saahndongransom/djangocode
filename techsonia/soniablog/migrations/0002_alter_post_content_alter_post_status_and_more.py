# Generated by Django 4.1.3 on 2022-12-09 22:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soniablog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]