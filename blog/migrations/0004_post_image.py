# Generated by Django 5.0.4 on 2024-04-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_body_alter_comment_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images', verbose_name='imagem'),
        ),
    ]
