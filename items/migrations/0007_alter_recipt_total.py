# Generated by Django 3.2.4 on 2021-07-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_recipt_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipt',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]