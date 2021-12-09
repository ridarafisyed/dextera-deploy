# Generated by Django 3.0.8 on 2021-12-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_classification_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=255, unique=True)),
                ('status', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
