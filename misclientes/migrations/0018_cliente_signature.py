# Generated by Django 2.0.6 on 2018-10-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0017_enterprise_enterprise_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='signature',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
