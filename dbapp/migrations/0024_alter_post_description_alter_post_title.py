# Generated by Django 4.1.3 on 2022-11-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0023_merge_0018_post_image_0022_scholarship_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
