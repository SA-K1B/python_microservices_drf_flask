# Generated by Django 5.1.2 on 2024-10-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_meals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.CharField(null=True),
        ),
    ]
