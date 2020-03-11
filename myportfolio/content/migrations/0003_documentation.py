# Generated by Django 2.2 on 2020-03-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200311_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('link_type', models.CharField(max_length=10, verbose_name='Тип ссылки')),
                ('link', models.URLField()),
            ],
        ),
    ]