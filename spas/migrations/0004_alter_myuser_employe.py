# Generated by Django 3.2.6 on 2021-08-11 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spas', '0003_alter_myuser_employe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='employe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='spas.employe'),
        ),
    ]