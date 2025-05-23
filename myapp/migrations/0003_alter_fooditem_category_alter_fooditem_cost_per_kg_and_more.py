# Generated by Django 5.2 on 2025-04-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_fooditem_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='cost_per_kg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='wastedata',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='wastedata',
            name='cost',
            field=models.FloatField(),
        ),
    ]
