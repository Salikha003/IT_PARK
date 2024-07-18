# Generated by Django 5.0.4 on 2024-05-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='reviews', verbose_name='Rasm')),
                ('name', models.CharField(max_length=255, verbose_name='Kompaniya nomi')),
                ('reviews', models.TextField(verbose_name='Fikrlar')),
            ],
        ),
    ]