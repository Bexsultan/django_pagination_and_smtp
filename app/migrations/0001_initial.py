# Generated by Django 4.0.4 on 2022-05-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, db_index=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='media', verbose_name='Фотки')),
            ],
        ),
    ]