# Generated by Django 3.2.6 on 2021-09-16 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spas', '0014_ligne_commande_prix_c'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mouvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_m', models.DateField()),
                ('qte', models.IntegerField()),
                ('type', models.CharField(choices=[('APPRO', 'APPRO'), ('SORTIE', 'SORTIE')], default='APPRO', max_length=8)),
                ('consommable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spas.consommable')),
                ('fourniture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spas.fourniture')),
                ('materiel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spas.materiel')),
            ],
        ),
    ]