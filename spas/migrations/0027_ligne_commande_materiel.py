# Generated by Django 3.2.6 on 2022-01-05 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spas', '0026_auto_20220105_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='ligne_commande',
            name='materiel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spas.materiel'),
        ),
    ]