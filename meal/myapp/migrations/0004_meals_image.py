# Generated by Django 5.1.2 on 2024-10-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_meals_mealid_alter_meals_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='image',
            field=models.ImageField(null=True, upload_to='./media'),
        ),
    ]