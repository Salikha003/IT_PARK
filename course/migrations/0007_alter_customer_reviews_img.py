# Generated by Django 5.0.4 on 2024-05-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_customer_reviews_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_reviews',
            name='img',
            field=models.ImageField(upload_to='reviews/', verbose_name='Rasm'),
        ),
    ]