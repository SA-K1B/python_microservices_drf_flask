# Generated by Django 5.1.2 on 2024-10-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealId', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('liked', models.BooleanField()),
            ],
        ),
    ]