# Generated by Django 5.0.4 on 2024-05-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='courses/', verbose_name='Rasmi')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
                ('about', models.TextField(verbose_name='Kurs haqida')),
                ('status', models.CharField(choices=[('deactive', 'deactive'), ('active', 'active')], default='deactive', max_length=50, verbose_name='Kurs holati')),
            ],
            options={
                'verbose_name': 'Kurslar',
                'verbose_name_plural': 'Kurslar',
                'db_table': 'CoursePage',
                'managed': True,
            },
        ),
    ]
