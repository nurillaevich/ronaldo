# Generated by Django 5.0.1 on 2024-01-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_comment_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
