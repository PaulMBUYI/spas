# Generated by Django 3.2.6 on 2022-01-05 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spas', '0027_ligne_commande_materiel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sortie',
            name='service',
        ),
    ]