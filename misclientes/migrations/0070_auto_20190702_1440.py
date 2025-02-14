# Generated by Django 2.0.6 on 2019-07-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misclientes', '0069_enterprise_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enterprise',
            options={'get_latest_by': ['contract'], 'ordering': ['-contract'], 'permissions': (('cambiar_enterprise', 'Puede Editar Empresas'),), 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='contract',
            field=models.IntegerField(default=0, verbose_name='Número de Contrato'),
        ),
    ]
