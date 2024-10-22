# Generated by Django 5.0.4 on 2024-05-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_why_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='team/', verbose_name='Rasmi')),
                ('name', models.CharField(max_length=255, verbose_name='Ism, Familiyasi')),
                ('about', models.TextField(verbose_name='Haqida')),
                ('telegram', models.URLField(verbose_name='Telegram akkaunt linki')),
                ('instagram', models.URLField(verbose_name='Instagram akkaunt linki')),
                ('github', models.URLField(verbose_name='Github akkaunt linki')),
            ],
            options={
                'verbose_name': 'Teachers',
                'verbose_name_plural': 'Teachers',
                'db_table': 'Teachers',
                'managed': True,
            },
        ),
    ]
