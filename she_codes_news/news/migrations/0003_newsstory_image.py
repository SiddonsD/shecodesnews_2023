# Generated by Django 4.2.7 on 2023-12-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
