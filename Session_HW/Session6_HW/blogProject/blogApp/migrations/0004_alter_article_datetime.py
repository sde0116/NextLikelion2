# Generated by Django 4.0.3 on 2022-04-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_alter_article_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
